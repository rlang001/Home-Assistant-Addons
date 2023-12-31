ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
RUN apt-get install -y wget gpg apt-transport-https expect
RUN apt install -y libfftw3-dev libglfw3-dev libvolk2-dev libsoapysdr-dev \
    libairspyhf-dev libiio-dev libad9361-dev librtaudio-dev libhackrf-dev
    

#RUN wget https://github.com/AlexandreRouma/SDRPlusPlus/releases/download/nightly/sdrpp_debian_bullseye_amd64.deb

#RUN dpkg -i sdrpp_debian_amd64.deb

# Debugging stuff
RUN apt-get install -y vim


#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

#########################################################
# Startup
# Right now weewx is started from run.sh
#########################################################
#COPY weewx.debian /etc/init.d/weewx
#RUN chmod +x /etc/init.d/weewx
#RUN update-rc.d weewx defaults 98

#########################################################
# 
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]