ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

#ENV OPENWEBRX_ADMIN_USER=ha
#ENV OPENWEBRX_ADMIN_PASSWORD=password

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
RUN apt-get install -y wget gpg nano apt-transport-https

RUN wget -O - https://repo.openwebrx.de/debian/key.gpg.txt | gpg --dearmor -o /usr/share/keyrings/openwebrx.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/openwebrx.gpg] https://repo.openwebrx.de/debian/ bullseye main" > /etc/apt/sources.list.d/openwebrx.list
RUN apt-get update
RUN apt-get install -y openwebrx


#########################################################
# Development stuff.  Not needed for operation
#########################################################
#RUN apt-get install -y nano


#########################################################
# SDR Stuff
#########################################################
# install rtl_433
# RUN apt-get install -y rtl-433

# Install the USB library
# RUN apt-get install -y libusb-1.0-0


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
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]