ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

RUN apt-get update  && apt-get -y upgrade

RUN apt-get install -y rtl-sdr wget rtl-433 python3 python3-paho-mqtt python3-yaml

WORKDIR /root

##########################################rtl_433###############
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################

COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]
