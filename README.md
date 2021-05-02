# Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
   - [Docker Tips and Tricks](#docker-tips-and-tricks)
   - [Mounting a Directory](#mounting-a-directory)
   - [Jupyter Notebooks](#Using-Jupyter-Notebooks-through-the-Docker-Image)
- [Notes for Windows Users](#notes-for-windows-users)
- [Graphics Forwarding from the Docker](#graphics-forwarding-from-the-docker)
   - [Graphics Forwarding for Ubuntu Users](#Ubuntu-X11-Forwarding-(Graphical-Usage))
   - [Graphics Forwarding for Windows Users](#Windows-X11-Forwarding-(Graphical-Options))
- [Notes for Developers](#notes-for-developers)
   - [Contribution](#how-to-contribute)
   - [DockerHub Link](#Link-to-the-latest-Docker-Image)
   - [Build Instructions](#building-the-docker-image)

# Prerequisites

- Install Docker ([Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://docs.docker.com/docker-for-windows/wsl/), [Mac](https://docs.docker.com/docker-for-mac/install/))
   - For Windows, make sure to get the latest version of Ubuntu (20.04), as it has been confirmed to work. Read on to see how to enable graphical interfacing in Windows.


# Quick Start
*This will work for both Ubuntu and Windows.*

Pull and run the latest image for the orientation. Open up a terminal and execute 

```shell
sudo docker run -it thomasmcelroy/saporientation
```

This command will produce a new container everytime it is run.

Once inside the container, execute `source env.sh` to get your environment ready (ROOT, GEANT4)

You can exit the container by typing `exit` or `ctrl+D`

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

## Naming Containers
You can name your containers when starting them up by doing

```shell
sudo docker run -it --name NAME thomasmcelroy/saporientation
```

where `NAME` is whatever you want to call your container. This way you can keep track of what your difference containers are for.

## Mounting a Directory 
You can mount a directory into the container so that you can write to your machine and save any results, notes etc... You produce in the container even after it is stopped and deleted.

```shell
sudo docker run -it -v /path/to/dir/onYourMachine/:/home/physuser/mountedDirectoryNameInDocker:rw thomasmcelroy/saporientation
```
Keep in mind that you may need to set the permissons on the folder you are mounting from your machine to read write and execute i.e. execute `chmod 777 /path/to/dir/onYourMachine` before mounting the volume.

## Using Jupyter Notebooks through the Docker Image
Start your Docker container with 

```shell
sudo docker run -it -p 8888:8888 --ip 0.0.0.0 thomasmcelroy/saporientation`. 
```
This maps the default port for Jupyter notebooks (`8888`) in the docker to your local machines `port 8888`.

Once inside the image, run 

```shell
jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token='sometoken'
```

On your browser, you can now go to `http://localhost:8888` and type in the "sometoken" you set in the jupyter notebook run command. Voila! Notebook away!

You can also add a `-v` flag to mount a directory with all your data from your machine into the docker by following the instructions in the section [Mounting a Directory](#mounting-a-directory)  and interact with that data using the notebook.

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

# Graphics Forwarding from the Docker

### Ubuntu X11 Forwarding (Graphical Usage)

If you want to use graphical interfaces, which can be incredibly convenient, you'll need to start by setting the correct permissions. Start with running

```shell
xhost local:root
```

in your terminal. Then, run docker with the following command

```shell
sudo docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix thomasmcelroy/saporientation
```

which we can see sets the display accordingly and mounts the X11 directory. 

### Windows X11 Forwarding (Graphical Options)
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
docker run -it -e DISPLAY=$DISPLAY -u root --name test thomasmcelroy/saporientation
```

This is assuming the `$DISPLAY` variable is set as the guide recommended. To check that it worked, repeat the above steps of installing graphical suite and running `xclock`.


# Notes For Developers
The rest of these notes are directed towards those who are hoping to contribute to the development of the docker image itself or its documentation. You do not need to worry about this section if you are a user. 

## Link to the latest Docker Image
DockerHub link: https://hub.docker.com/r/thomasmcelroy/saporientation 


## Building the Docker Image:

You can build the docker image yourself by doing `docker build -t <tagname> ./ `

This command will take a couple hours to run. The final image will be 8-9 GB so beware! 

You can then run `docker images` to see all your downloaded images. Take note of the Image ID for the sap orientation image. 

Run `sudo docker build -t [Image ID] ./` to build the image.

## How to Contribute 
If you would like to contribute to this image, please open an issue on the repository on GitHub and you will be given permissions to modify the files. 

### List of Contributors
- Thomas McElroy 
- Soud Al Kharusi
- Dilraj Ghuman