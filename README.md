Prep:
1. Install Docker
2. Clone Git repository
3. In repository folder run: git submodule update --init --recursive

Build:
docker build -t <tagname> ./

THis will take a couple hours and the final image will be 7-8 GB. 


Directly pull image:
docker pull thomasmcelroy/saporientation

once inside container run "source env.sh" to setup root and geant environment variables.


DockerHub: https://hub.docker.com/r/thomasmcelroy/saporientation 
