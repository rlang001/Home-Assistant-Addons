ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Development stuff.  Not needed for operation
#########################################################
#RUN apt-get install -y nano


#########################################################
# SDR Stuff
#########################################################
# install rtl_433
RUN apt-get install -y rtl-433

# Install the USB library
RUN apt-get install -y libusb-1.0-0


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
# 
#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]