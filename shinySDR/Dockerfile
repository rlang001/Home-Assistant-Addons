ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
# python
RUN apt-get install -y python-is-python2 pip git


# GNU radio
RUN apt-get install -y gnuradio

RUN cd ~; git clone https://github.com/kpreid/shinysdr/

#RUN pip install twisted
#RUN pip install six
#RUN pip install txws
#RUN pip install pyephem
#RUN pip install pyserial


# gr-osmosdr
# RUN apt-get install -y 

#RUN apt-get install -y sqlite3 wget sudo supervisor tzdata jq nginx

#      python-is-python3 python3-pip python3-configobj python3-cheetah python3-pil python3-serial python3-usb python3-ephem python3-setuptools \

#########################################################
# Need for weewx-nws
#########################################################
#RUN apt-get install -y python3-dateutil

#########################################################
# Development stuff.  Not needed for operation
#########################################################
#RUN apt-get install -y nano

#########################################################
# Some python reqs
#########################################################
#RUN pip3 install pyserial requests

#RUN wget https://github.com/anastas78/weewx-mqtt/archive/refs/heads/ha-discovery-with-lwt.zip -O /tmp/weewx-mqtt.zip && \

#     cd /tmp && \
#      /home/weewx/bin/wee_extension --install weewx-mqtt.zip


#########################################################
# Download/install the SDR driver
#########################################################
#RUN wget https://github.com/matthewwall/weewx-sdr/archive/master.zip -O /tmp/weewx-sdr.zip && \
#      cd /tmp && \
#      /home/weewx/bin/wee_extension --install weewx-sdr.zip

#########################################################
# SDR Stuff
#########################################################
# install rtl-sdr
#RUN apt-get update
#RUN apt-get install -y rtl-sdr

# install rtl_433
#RUN apt-get install -y rtl-433


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
