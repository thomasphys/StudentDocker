Prep:
1. Install Docker
2. In a folder pull the latest ROOT into a folder labelled root and GEANT4 into a folder with the Dockerfile.
with git:
git clone git@github.com:Geant4/geant4.git
git clone git@github.com:root-project/root.git

Build:
docker build -t <tagname> ./

THis will take a couple hours and the final image will be 7-8 GB. 

