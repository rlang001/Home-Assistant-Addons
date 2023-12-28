ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt upgrade -y

#########################################################
# Install prerequisites
#########################################################
RUN apt-get install -y wget git git-man libcurl3-gnutls liberror-perl

#########################################################
# SDR Stuff
#########################################################
# install rtl-sdr
RUN apt-get update
RUN apt-get install -y rtl-sdr


#########################################################
# Development stuff.  Not needed for operation
#########################################################
RUN apt-get update
RUN apt-get install -y nano


#########################################################
# SDR Stuff
# Do this instead of building below?
#########################################################
# install rtl-sdr
#RUN apt-get update
#RUN apt-get install -y rtl-sdr

#########################################################
# SDR / Dump1090 Stuff
#########################################################
# install rtl-sdr

# RUN apt-get install -y rtl-sdr
# Stuff to build dump1090 
#RUN apt-get install -y git cmake libusb-1.0-0-dev pkg-config
#RUN cd /root; git clone https://git.osmocom.org/rtl-sdr.git
#RUN cd /root/rtl-sdr; cmake ./ -DINSTALL_UDEV_RULES=ON
#RUN cd /root/rtl-sdr; make
#RUN cd /root/rtl-sdr; make install


#RUN cd /root; git clone https://github.com/rlang001/dump1090.git
#RUN cd /root/dump1090; make

# Install
#RUN bash -c "$(wget -nv -O - https://github.com/wiedehopf/tar1090/raw/master/install.sh)"


#########################################################
# Remove nginx config, temp stuff
#########################################################
#RUN rm -fr \
#    /etc/nginx \
#    /tmp/*
    
# Copy root filesystem
COPY rootfs /

#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]