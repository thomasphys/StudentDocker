# Prerequisites
Install Docker ([Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://docs.docker.com/docker-for-windows/wsl/),  )
   - For Windows, make sure to get the latest version of Ubuntu (20.04), as it has been confirmed to work.



# Quick Start
This will work for both Ubuntu and Windows.

Pull and run the latest image for the orientation.  

`sudo docker run -it thomasmcelroy/saporientation`

This command will produce a new container everytime it is run.

Execute `source env.sh` to get your environment ready (ROOT, GEANT4)

You can detach from the container by doing `ctrl+p` then `ctrl+q` and rejoin later. 

View all running containers `sudo docker container ls` or add a `-a` flag at the end to view all (including stopped containers)

Attached to a running container with `sudo docker attach [CONTAINER ID]`

Exit the container by doing `ctrl+d` or typing `exit` when in the container. 

Delete all the stopped containers on your system with them by doing `sudo docker container prune`

Alternatively, close only the container you want by `sudo docker container rm [CONTAINER ID]`. If the container is running it will not close, so you will have to either attach to it and exit it or use `sudo docker container rm -f [CONTAINER ID]`

You can name your containers upon running,

`sudo docker run -it --name NAME thomasmcelroy/saporientation`

where `NAME` is whatever you want to call your container. This way you can run the same container for later use without creating too many containers.

### Mounting a directory 
You can mount a directory into the container so that you can write to your machine and save any results, notes etc... You produce in the container even after it is stopped and deleted.

`sudo docker run -it -v /path/to/dir/onYourMachine/:/home/physuser/mountedDirectoryNameInDocker:rw thomasmcelroy/saporientation`

Keep in mind that you may need to set the permissons on the folder you are mounting from your machine to read write and execute i.e. execute `chmod 777 /path/to/dir/onYourMachine` before mounting the volume.

## Using Jupyter Notebooks through the Docker Image
Start your Docker container with `sudo docker run -it -v /home/soud/McGill/StudentDocker/:/home/physuser/mountedDirectory:rw -p 8888:8888 --ip 0.0.0.0 thomasmcelroy/saporientation`. 

Once inside the image, run `jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.token='sometoken'`

On your browser, you can now go to `http://localhost:8888` and type in the "sometoken" you set in the jupyter notebook run command. Voila! Notebook away!

## Link to the latest Docker Image
DockerHub link: https://hub.docker.com/r/thomasmcelroy/saporientation 

## Notes for Windows Users
It is important to go through the instructions outlined in the Docker installation in the order described. 

In order for the Windows Subsystem for Linux (WSL) to work with the Docker application, you need them both to be running simultaneously.

The Docker GUI will also provide a simple way to see what current images are available and what containers are running.

It is recommended you use the CLI through the WSL Ubuntu application. 

WSL can take a lot of resources to run, so be cognisent of this. Moreover, if you have Task Manager running in the back, you'll see just how much of your resources are being used.

When closing your instances, note that simply closing the window may not be enough. To end the `Vmmem` task (which is the virtual machine), run

`wsl --shutdown`

in PowerShell. 

## How to Contribute 
If you would like to contribute to this image, please open an issue on the repository on GitHub and we will allow you to branch off and develop your code. 

### List of Contributors
- Thomas McElroy 
- Soud Al Kharusi
- Dilraj Ghuman

# Deprecated
## Prep:
1. Install Docker ([Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://docs.docker.com/docker-for-windows/wsl/),  )
   - For Windows, make sure to get the latest version of Ubuntu (20.04), as it has been confirmed to work.
2. Clone this GitHub repository
3. From your terminal, navigate this repository and run `git submodule update --init --recursive`
   - This gets you the latest ROOT and Geant4 packages when building the Docker Image.  

## Building the Docker Image:

You can build the docker image yourself by doing `docker build -t <tagname> ./ `

This command will take a couple hours to run. The final image will be 8-9 GB so beware! 

## Directly pulling the latest image:
If you don't want to build the image directly then you can instead do `docker pull thomasmcelroy/saporientation` which pulls the latest image on the DockerHub. 

You can then run `docker images` to see all your downloaded images. Take note of the Image ID for the sap orientation image. 

Run `sudo docker build -t [Image ID] ./` to build the image.
