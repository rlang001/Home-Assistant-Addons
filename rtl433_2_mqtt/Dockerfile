ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

RUN apt-get update 

# install build system
# RUN apt-get install -y software-properties-common libtool libusb-1.0-0-dev \
#    librtlsdr-dev libssl-dev rtl-sdr build-essential cmake pkg-config  git

RUN apt-get install -y software-properties-common rtl-sdr

# Get repository 
# WORKDIR /root
# RUN git clone https://github.com/merbanan/rtl_433.git

# Build rtl-433
# WORKDIR /root/rtl_433
# RUN cmake -B build && \
#    cmake --build build --target install
    
#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################

#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]



