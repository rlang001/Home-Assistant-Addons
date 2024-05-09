ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV MAKEFLAGS='-j 8'

# Ensure that we always use UTF-8, US English locale and UTC time
RUN apt-get update && apt-get install -y locales && \
      localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
      echo "UTC" > /etc/timezone && \
      chmod 0755 /etc/timezone 

ENV LANG=en_US.utf8
ENV LC_ALL=en_US.utf-8
ENV LANGUAGE=en_US:en
ENV PYTHONIOENCODING=utf-8


RUN apt-get update

# && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
# python
RUN apt-get install -y python-is-python3 python3-pip\
      gnuradio gnuradio-dev \ 
      gr-osmosdr \
      git


#RUN pip install setuptools

RUN pip install twisted
#RUN pip install six
RUN pip install txws
RUN pip install pyephem
RUN pip install pyserial

WORKDIR /root
RUN git clone https://github.com/kpreid/shinysdr/

WORKDIR /root/shinysdr
RUN z

#RUN python setup.py install

#python-is-python3 python3-pip python3-configobj python3-cheetah python3-pil python3-serial python3-usb python3-ephem python3-setuptools \


#####################################
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
