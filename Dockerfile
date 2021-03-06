FROM ubuntu:20.04

MAINTAINER Thomas McElroy

# Explicitly become root (even though likely we are root already)
USER root

ARG ROOT_VERSION=6.24.04 #this does not do anything right now
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y \
    python3 python3-dev python3-pip curl \
    git vim-gtk dpkg-dev cmake g++ gcc binutils libx11-dev \
    libxpm-dev libxft-dev libxext-dev sudo -qqy x11-apps gedit \
    gedit-plugin-draw-spaces \
    silversearcher-ag \
    evince \
    eog && \
    rm -rf /var/lib/apt/lists/*

RUN  apt install -y python3-pip fftw3-dev & \
     pip3 install --upgrade pip setuptools && \
     # make some useful symlinks that are expected to exist
     if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
     if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python3-config /usr/bin/python-config; fi && \
     if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3 /usr/bin/pip; fi &&\
     pip3 install Numpy Pandas Matplotlib Scikit-Learn Scipy jupyterlab tensorflow astropy

##Install root
WORKDIR /root
COPY root ./root
RUN mkdir /opt/root && \
	    cd /opt/root && \
	    cmake -Dxrootd=OFF -Dbuiltin_xrootd=OFF ${HOME}/root/ -DPYTHON_EXECUTABLE=/usr/bin/python3 && \
	    make -j4 && \
	    rm -r ${HOME}/root/ && \
	    cd    

# Install dependencies for Geant4
RUN apt-get update && apt-get install -y libxerces-c3-dev freeglut3-dev libmotif-dev tk-dev cmake libxpm-dev libxmu-dev libxi-dev

WORKDIR /geant4
COPY geant4 /opt/geant4

RUN mkdir /opt/geant4/build && \
	    cd /opt/geant4/build && \
	    cmake -DCMAKE_INSTALL_PREFIX=/opt/geant4/ -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON /opt/geant4/ &&\
	    cmake --build . -- -j8  && \
	    cmake --build . --target install

# non needed for most
RUN apt-get update && apt-get install -y libtet1.5-dev libassimp-dev wget

# Create user
RUN useradd -m physuser 
RUN passwd -d physuser #remove the password from the user
RUN adduser physuser sudo #add user to sudo group so they can install stuff if needed on the fly
RUN mkdir -p /home/physuser
RUN chown -R physuser:physuser /home/physuser
ENV DISPLAY :0

# Become that user
USER physuser
COPY env.sh /home/physuser/
WORKDIR /home/physuser

