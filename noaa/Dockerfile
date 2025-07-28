ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG=C.UTF-8
ENV TZ=UTC


#########################################################
# Required packages and software
#########################################################

RUN apt-get update 
RUN apt-get install -y vim git python3 sudo expect

# Add the noaa user
RUN useradd -d /home/noaa -p $(openssl passwd -1 password) noaa
RUN usermod -aG sudo noaa


USER noaa

# clone repository
WORKDIR /home/noaa
RUN  git clone --depth 1 https://github.com/jekhokie/raspberry-noaa-v2.git
WORKDIR /home/noaa/raspberry-noaa-v2/
# RUN 


# perform install
# Currently this is failing during install
# ./install_and_upgrade.sh


USER root
#$RUN apt-get install -y git python-is-python3 python3-pip

#RUN pip install pyyaml


#COPY rootfs /
#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]