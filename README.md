# Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
   - [Notes for Windows Users](#notes-for-windows-users)
- [Docker Tips and Tricks](#docker-tips-and-tricks)
   - [Detaching from Containers](#detaching-from-containers)
   - [Mounting a Directory](#mounting-a-directory)
   - [Jupyter Notebooks](#Using-Jupyter-Notebooks-through-the-Docker-Image)
- [Graphics Forwarding from the Docker](#graphics-forwarding-from-the-docker)
   - [Graphics Forwarding for Ubuntu Users](#Ubuntu-X11-Forwarding)
   - [Graphics Forwarding for Windows Users](#Windows-X11-Forwarding)
   - [Graphics Forwarding for MacOS Users](#MacOS-X11-Forwarding)
- [Notes for Developers](#notes-for-developers)
   - [Contribution](#how-to-contribute)
   - [DockerHub Link](#Link-to-the-latest-Docker-Image)
   - [Build Instructions](#building-the-docker-image)

# Prerequisites
- Around 10 GB of free space on your system.
- Install Docker ([Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://docs.docker.com/docker-for-windows/wsl/), [Mac](https://docs.docker.com/docker-for-mac/install/))
   - For Windows, make sure to get the latest version of Ubuntu (20.04) for WSL, as it has been confirmed to work. 

# Quick Start

Pull and run the latest image for the orientation: 

open up a terminal and execute 

```shell
sudo docker run -it soudk/eieioo2021
```
which will download the container the first time, but otherwise just run the container once it's on your machine without downloading anything.

Once inside the container, execute `source env.sh` to get your environment ready (ROOT, GEANT4)

You can exit the container by typing `exit` or `ctrl+D`

If you'd like graphics forwarding to your screen, you will need to follow the instruction set out for your system in the section [Graphics Forwarding from the Docker](#graphics-forwarding-from-the-docker).

## Notes for Windows Users
 Go through the instructions outlined in the Docker installation in the order described. 

In order for the Windows Subsystem for Linux (WSL) to work with the Docker application, you need them both to be running simultaneously.

The Docker GUI will also provide a simple way to see what current images are available and what containers are running.

It is recommended you use the CLI through the WSL Ubuntu application. 

WSL can take a lot of resources to run, so be cognisent of this. Moreover, if you have Task Manager running in the back, you'll see just how much of your resources are being used.

When closing your instances, note that simply closing the window may not be enough. To end the `Vmmem` task (which is the virtual machine), run

```shell
wsl --shutdown
```

in PowerShell. 

# Docker Tips and Tricks

## List all Containers

You can view all running containers on your system by doing `sudo docker container ls` or add a `-a` flag at the end to view all (including stopped containers). Take note of the `CONTAINER ID` field.

## Detaching from Containers
Instead of exiting from a container, you can detach from it by doing `ctrl+p` then `ctrl+q`. This will allow you to rejoin the same container later an pick up where you left off. 

You can reattach to a running container with 

```shell
sudo docker attach [CONTAINER ID]
```

using the ID you found when listing all your running containers.


## Mounting a Directory 
You can mount a directory into the container so that you can write to your machine and save any results, notes etc... You produce in the container even after it is stopped and deleted.

```shell
sudo docker run -it -v /path/to/dir/onYourMachine/:/home/physuser/mountedDirectoryNameInDocker:rw soudk/eieioo2021
```
Keep in mind that you may need to set the permissons on the folder you are mounting from your machine to read write and execute i.e. execute `chmod 777 /path/to/dir/onYourMachine` before mounting the volume.

## Using Jupyter Notebooks through the Docker Image
Start your Docker container with 

```shell
sudo docker run -it -p 8888:8888 --ip 0.0.0.0 soudk/eieioo2021 
```
This maps the default port for Jupyter notebooks (`8888`) in the docker to your local machines `port 8888`.

Once inside the image, run 

```shell
jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token='sometoken'
```

On your browser, you can now go to `http://localhost:8888` and type in the "sometoken" you set in the jupyter notebook run command. Voila! Notebook away!

You can also add a `-v` flag to mount a directory with all your data from your machine into the docker by following the instructions in the section [Mounting a Directory](#mounting-a-directory)  and interact with that data using the notebook.

## Naming Containers
You can name your containers when starting them up by doing

```shell
sudo docker run -it --name NAME soudk/eieioo2021
```

where `NAME` is whatever you want to call your container. This way you can keep track of what the different containers on your system are for.

## Cleaning up your Containers
Delete all the stopped containers on your system with them by doing 

```shell
sudo docker container prune
```

Which will clear up resources from your system.

Alternatively, close only the container you want by

```shell
sudo docker container rm [CONTAINER ID]
```
 
If the container is running it will not close, so you will have to either attach to it and exit it or use 
  
```shell
sudo docker container rm -f [CONTAINER ID]
```

to force it to close and be removed.

# Graphics Forwarding from the Docker

If you want to use graphical interfaces, which can be incredibly convenient, you will need to follow the instruction below for your system. 

## Ubuntu X11 Forwarding 

Start with running

```shell
xhost local:root
```

in your terminal. Then, run docker with the following command

```shell
sudo docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix soudk/eieioo2021
```

which we can see sets the display accordingly and mounts the X11 directory. 

Note that you will have to `xhost local:root` everytime you open a new terminal and want to do X11 forwarding with docker. 

## Windows X11 Forwarding 
Windows is a bit annoying for getting graphical options running,since things were changed with the move to Windows Subsystem for Linux 2 (WSL2). Regardless, the first thing you'll want to do is update your package options by running

```shell
sudo apt update
```

in your WSL2 terminal. Then you'll get the graphical suite by running

```shell
sudo apt install x11-apps
```

Now the tough part begins. This will involve giving the terminal access through your firewall. I found following [this](https://skeptric.com/wsl2-xserver/) guide to work. Note it will require you to install VcXsrv aswell.

VcXsrv creates a virtual session for your ubuntu subsystem to forward to and will need to be run each time beforehand. The instructions give a command to run VcXsrv using the powershell, which I found worked for me in the following form:

```shell
& 'D:\Programs\VcXsrv\vcxsrv.exe' :0 -multiwindow -wgl -ac
```

The pathway here will be different for you, just change it to where the program was installed. If this is too complicated, you can also just run the XLaunch application that is used to run VcXsrv. In that case, select "Multiple Windows > Start no client > Disable access control", where the first two options are the defaults, and the last option we enable that extra choice (Don't disable anything). You can save this when it asks, but that isn't necessary.  

Once you have followed the instructions to completion, run `sudo apt install x11-apps` and check that the X11 forwarding works by running `xclock` in your terminal. This should pop up an anologue clock on your screen.

If the clock appears on your screen, you are pretty much done! The only difference is that when you are running your docker client, I found starting it using the following command set up the proper display,

```shell
docker run -it -e DISPLAY=$DISPLAY soudk/eieioo2021
```

This is assuming the `$DISPLAY` variable is set as the guide recommended. To check that it worked, repeat the above steps of installing graphical suite and running `xclock`.


## MacOS X11 Forwarding 
You will need to install XQuartz version >2.7.10, you can do this with homebrew or by installing a .dmg file

### Homebrew method
Install homebrew by following the instructions [here](https://brew.sh/).

Next, you'll want to get XQuartz version >2.7.10 by running 

```shell
brew install xquartz
``` 

in your terminal.

### Installing the .dmg
You can find and install the .dmg file [here](https://www.xquartz.org/).

Once you have XQuartz installed (using either homebrew or .dmg method) you can follow the instructions below.

Run `open -a XQuartz` and click on the XQuartz logo that popped up in your dock. 

Go to XQuartz (top left of your screen) then Preferences. 

Click on the Security Tab in Preferences, and checkmark the "allow conections from network clients" box.

Close the Preferences window and then close XQuartz by quitting it from the dock.

Run XQuartz again with

```shell
open -a XQuartz
```

Then run the command 

```shell
xhost + 127.0.0.1
```
which will allow docker to access your screen. 

*Note: if you quit XQuartz you will have to allow docker access to your screen again with* `xhost + 127.0.0.1` *again*.

Now you can run your docker image with the flag `-e DISPLAY=host.docker.internal:0`

So for this docker image

```shell
sudo docker run -it -e -e DISPLAY=host.docker.internal:0 soudk/eieioo2021
```

You can run `xclock` once inside the docker image to check that the graphics forwarding is working properly.


# Notes For Developers
The rest of these notes are directed towards those who are hoping to contribute to the development of the docker image itself or its documentation. You do not need to worry about this section if you are a user. 

## Link to the latest Docker Image
DockerHub link: https://hub.docker.com/r/soudk/eieioo2021 


## Building the Docker Image:

After cloning the StudentDocker repository into your machine, you will need to run 

```shell
git submodule sync
```

then 

```shell
git submodule update --init --recursive
```
To populate the GEANT4 and ROOT submodules in the repository.

finally, update the modules with

```shell
git submodule update --remote --merge
```

You can then build the docker image yourself by doing 

```shell
docker build -t [IMAGE NAME] ./ 
```

where `[IMAGE NAME]` is whatever you want to call your image (must be all lower case).

This command will take a couple hours to run. The final image will be 8-9 GB so beware! If you don't want to wait forever, you can edit the `Dockerfile` nd comment out the ROOT and GEANT4 parts, but this will leave you with an image without either softwares. 

Run `sudo docker build -t [IMAGE NAME] ./` to build the image.

After you build the image, you can run `docker images` to see all your downloaded images. Take note of the `[IMAGE ID]` for your new image. 

Then run your new container by doing 

```shell
sudo docker run -it [IMAGE NAME]
```

You can also replace `[IMAGE NAME]` with the `[IMAGE ID]` you saw when you listed all your images earlier.

## How to Contribute 
If you would like to contribute to this image, please open an issue on the repository on GitHub and you will be given permissions to modify the files. 

### List of Contributors
- Thomas McElroy 
- Soud Al Kharusi
- Dilraj Ghuman
