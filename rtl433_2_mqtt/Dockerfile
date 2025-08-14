ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

RUN apt-get update

# install build system
# RUN apt-get install -y software-properties-common libtool libusb-1.0-0-dev \
#    librtlsdr-dev libssl-dev rtl-sdr build-essential cmake pkg-config  git

RUN apt-get install -y software-properties-common rtl-sdr wget python3.12 \
    python3-paho-mqtt python3-yaml

WORKDIR /root

#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /
RUN ldconfig

########################################################
# Modify the existing /run.sh file
########################################################

COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]
