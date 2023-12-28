ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update

#########################################################
# Install prerequisites
#########################################################
RUN apt-get install -y sqlite3 wget sudo \
      python-is-python3 python3-pip python3-configobj python3-cheetah python3-pil python3-serial python3-usb python3-ephem python3-setuptools \
      supervisor tzdata jq nginx 

#########################################################
# Need for weewx-nws
#########################################################
RUN apt-get install -y python3-dateutil

#########################################################
# Development stuff.  Not needed for operation
#########################################################
RUN apt-get install -y nano

#########################################################
# Some python reqs
#########################################################
RUN pip3 install pyserial requests

#########################################################
# Install WeeWx
#########################################################
RUN wget http://weewx.com/downloads/released_versions/weewx-4.10.2.tar.gz -O /tmp/weewx.tgz && \
      cd /tmp && \
      tar zxvf /tmp/weewx.tgz && \
      cd weewx-* ; ./setup.py build ; ./setup.py install --no-prompt

#########################################################
# Install MQTT stuff
#########################################################
RUN wget https://github.com/eclipse/paho.mqtt.python/archive/v1.6.1.tar.gz -O /tmp/mqtt.tgz && \
      cd /tmp && \
      tar zxvf /tmp/mqtt.tgz && \
      cd paho.mqtt.python-* ; sudo python3 setup.py build ; sudo python3 setup.py install

#########################################################
# WeewWX-MQTT with HA discovery
#########################################################


RUN wget https://github.com/anastas78/weewx-mqtt/archive/refs/heads/ha-discovery-with-lwt.zip -O /tmp/weewx-mqtt.zip && \

      cd /tmp && \
      /home/weewx/bin/wee_extension --install weewx-mqtt.zip

#########################################################
# install MQTT-Subscribe
#########################################################
RUN wget https://github.com/bellrichm/WeeWX-MQTTSubscribe/archive/refs/tags/v2.2.2.zip -O /tmp/WeeWX-MQTTSubscribe.zip && \
      cd /tmp && \
      MQTTSubscribe_install_type=SERVICE /home/weewx/bin/wee_extension --install WeeWX-MQTTSubscribe.zip


#########################################################
# Download/install the SDR driver
#########################################################
RUN wget https://github.com/matthewwall/weewx-sdr/archive/master.zip -O /tmp/weewx-sdr.zip && \
      cd /tmp && \
      /home/weewx/bin/wee_extension --install weewx-sdr.zip

#########################################################
# Download/install NWS forecast
#########################################################
RUN wget https://github.com/chaunceygardiner/weewx-nws/releases/download/v2.3/weewx-nws-2.3.zip -O /tmp/weewx-nws.zip && \
      cd /tmp && \
      /home/weewx/bin/wee_extension --install weewx-nws.zip

#########################################################
# SDR Stuff
#########################################################
# install rtl-sdr
RUN apt-get update
RUN apt-get install -y rtl-sdr

# install rtl_433
RUN apt-get install -y rtl-433

#########################################################
# Download/install some skins
#########################################################
# NeoWIX-Material skin
# We are now embedding this skin 
#RUN wget https://neoground.com/neowx-material/download/latest -O /tmp/neowx-material-latest.zip && \
#      cd /tmp && \
#      /home/weewx/bin/wee_extension --install neowx-material-latest.zip

# Steel Series skin
# We are now embedding this skin 
#RUN wget https://github.com/gjr80/weewx-steelseries/releases/download/v2.7.6/steelseries-2.7.6.tar.gz -O /tmp/steelseries.tar-gz && \
#      cd /tmp && \
#      /home/weewx/bin/wee_extension --install steelseries.tar-gz

# Amphibian Skin
# We are now embedding this skin 
#RUN wget https://github.com/matthewwall/weewx-amphibian/archive/master.zip -O /tmp/weewx-amphibian.zip  && \
#      cd /tmp && \
#      /home/weewx/bin/wee_extension --install weewx-amphibian.zip


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