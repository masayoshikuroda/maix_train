FROM ubuntu:20.04

RUN apt update
RUN apt install -y zip unzip
RUN apt install -y tzdata
RUN apt install -y git
RUN apt install -y libopencv-dev
RUN apt install -y libgl1-mesa-dev

RUN apt install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip

WORKDIR /root
RUN git clone https://github.com/sipeed/maix_train.git
WORKDIR /root/maix_train
COPY __init__.py train/
RUN pip3 install -r requirements.txt

RUN apt install -y curl
RUN apt install -y xz-utils
RUN mkdir -p tools/ncc/ncc_v0.1
WORKDIR tools/ncc/ncc_v0.1
RUN curl -LO https://github.com/kendryte/nncase/releases/download/v0.1.0-rc5/ncc-linux-x86_64.tar.xz
RUN tar Jxfv ncc-linux-x86_64.tar.xz
RUN rm ncc-linux-x86_64.tar.xz

WORKDIR /root/maix_train
RUN python3 train.py init
