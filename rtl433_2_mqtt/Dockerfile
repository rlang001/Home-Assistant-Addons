ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC



RUN apt-get update 
# && apt-get upgrade -y
RUN apt-get install -y software-properties-common libtool libusb-1.0-0-dev \
    librtlsdr-dev libssl-dev rtl-sdr build-essential cmake pkg-config  git


# libssl-dev

WORKDIR /root
RUN git clone https://github.com/merbanan/rtl_433.git


# Get the latest rtl-433 and 
WORKDIR /root/rtl_433
RUN cmake -B build && \
    cmake --build build --target install
    
#########################################################
# Copy data for add-on to docker fs
#########################################################
# COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################
# # Create the directory if needed
#RUN sed -i 's/#listen   80;/listen   8099;/g' /etc/nginx/sites-available/default
#RUN sed -i 's;supervisord;i mkdir -p /config/syslog;g' /run.sh


#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]



