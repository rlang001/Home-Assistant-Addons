ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y libusb-1.0-0


#########################################################
COPY rootfs /

#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]
