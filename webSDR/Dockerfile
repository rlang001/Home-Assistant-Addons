ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
# RUN apt-get install -y wget iproute2 

#RUN apt-get install -y sqlite3 wget sudo \
#      python-is-python3 python3-pip python3-configobj python3-cheetah python3-pil python3-serial python3-usb python3-ephem python3-setuptools \
#      supervisor tzdata jq nginx 

#########################################################
# Development stuff.  Not needed for operation
#########################################################
#RUN apt-get install -y nano


#########################################################
# SDR Stuff
#########################################################

# Install the USB library
# RUN apt-get install -y libusb-1.0-0

# Install Go
# RUN wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
# RUN tar -zxvf go1.21.5.linux-amd64.tar.gz
# RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# RUN go install github.com/bemasher/rtlamr@latest


#########################################################
# Remove nginx config, temp stuff
#########################################################
RUN rm -fr \
      /etc/nginx \
      /tmp/*

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
#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]