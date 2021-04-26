## Prep:
1. Install Docker ([Ubuntu](https://docs.docker.com/engine/install/ubuntu/), ,  )
2. Clone this GitHub repository
3. From your terminal, navigate this repository and run `git submodule update --init --recursive`
   - This gets you the latest ROOT and Geant4 packages when building the Docker Image.  

## Building the Docker Image:

You can build the docker image yourself by doing `docker build -t <tagname> ./ `

This command will take a couple hours to run. The final image will be 8-9 GB so beware! 

## Directly pulling the latest image:
If you don't want to build the image directly then you can intead do `docker pull thomasmcelroy/saporientation` which pulls the latest image on the DockerHub. 

You can then run `docker images` to see all your downloaded images. Take note of the Image ID for the sap orientation image. 

Run `sudo docker build -t [Image ID] ./` to build the image.

## Using the Image
Once inside the container, run `source env.sh` to setup ROOT and Geant4 environment variables.

## Fastest way to get going
Pull and run the latest image for the orientation.  

`sudo docker run -it thomasmcelroy/saporientation`

Execute `source env.sh` to get your environment ready (ROOT, GEANT4)

You can detach from the container by doing `ctrl+p` then `ctrl+q` and rejoin later. 

View all running containers `sudo docker container ls` or add a `-a` flag at the end to view all (including stopped containers)

Attached to a running container with `sudo docker attach [CONTAINER ID]`

Exit the container by doing `ctrl+d` or typing `exit` when in the container. 

Delete all the stopped containers on your system with them by doing `sudo docker container prune`

Alternatively, close only the container you want by `sudo docker container rm [CONTAINER ID]`. If the container is running it will not close, so you will have to either attach to it and exit it or use `sudo docker container rm -f [CONTAINER ID]`

DockerHub link: https://hub.docker.com/r/thomasmcelroy/saporientation 

## How to Contribute 


### List of Contributors
