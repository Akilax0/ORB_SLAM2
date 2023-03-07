FROM ubuntu:18.04
LABEL maintainer="Akilax0"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Colombo

# installing required tools
RUN apt-get update


RUN apt-get install -y tzdata
RUN apt-get install -y libglew-dev cmake build-essential libtbb-dev \
    libeigen3-dev doxygen unzip wget \
    zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev \
    libopenexr-dev libgdal-dev vim git \
    qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools \
    python-pip python3-dev python3-tk python3-numpy \
    ant default-jdk

# set geographical area and country for timezone when prompted

# Pangolin v0.5 build 
RUN mkdir packages && cd packages && \
    git clone https://github.com/stevenlovegrove/Pangolin.git && \
    cd Pangolin && \
    git checkout tags/v0.5 -b v0.5-branch && \
    mkdir build && cd build && \
    cmake .. && make -j$(nproc) && \
    cd .. 


# OpenCV v3.2 build 
RUN cd packages && wget https://github.com/opencv/opencv/archive/3.2.0.zip \
    -O OpenCV320.zip && unzip OpenCV320.zip && cd opencv-3.2.0 && \
    mkdir build && cd build && \
    cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON \
    -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON \
    -DENABLE_PRECOMPILED_HEADERS=OFF .. && make -j$(nproc) && \
    make install && ldconfig && \
    cd ..

# ORB_SLAM2 build from Akilax0
RUN git clone https://github.com/Akilax0/ORB_SLAM2.git 

RUN cd ORB_SLAM2 && sh build.sh 
