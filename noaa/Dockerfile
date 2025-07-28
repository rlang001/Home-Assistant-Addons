ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

#########################################################
# Required packages and software
#########################################################

RUN apt-get update 
#RUN apt-get install -y nano vim

RUN apt-get install -y git python-is-python3 python3-pip

RUN pip install pyyaml

# clone repository
# cd $HOME
RUN cd $HOME; git clone https://github.com/jekhokie/raspberry-noaa-v2.git
#cd raspberry-noaa-v2/

COPY rootfs /
#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]