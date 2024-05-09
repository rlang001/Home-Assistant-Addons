
ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt upgrade -y

#########################################################
# Install prerequisites
#########################################################
RUN apt-get update
RUN apt-get install -y wget nginx

#########################################################
# Development stuff.  Not needed for operation
#########################################################
RUN apt-get install -y nano vim

#########################################################
# SDR Stuff
# Do this instead of building below?
#########################################################
# install rtl-sdr
RUN apt-get update
#RUN apt-get install -y rtl-sdr 

# Stuff to build dump1090
RUN apt-get install -y build-essential fakeroot debhelper librtlsdr-dev pkg-config \
    libncurses5-dev libbladerf-dev libhackrf-dev liblimesuite-dev \ 
    libsoapysdr-dev curl

RUN apt-get install -y git cmake libusb-1.0-0-dev 

WORKDIR /root
RUN apt-get install --no-install-recommends --no-install-suggests -y \
    git build-essential debhelper libusb-1.0-0-dev \
    librtlsdr-dev librtlsdr0 pkg-config \
    libncurses-dev zlib1g-dev zlib1g libzstd-dev libzstd1

#######################################################################
# Install readsb
#######################################################################
RUN git clone --depth 20 https://github.com/wiedehopf/readsb.git
WORKDIR /root/readsb
ENV DEB_BUILD_OPTIONS=noddebs
RUN dpkg-buildpackage -b -Prtlsdr -ui -uc -us
RUN dpkg -i ../readsb_*.deb


#######################################################################
# tar1090
#######################################################################
WORKDIR /tmp
#RUN bash -c "$(wget -nv -O - https://github.com/wiedehopf/tar1090/raw/master/install.sh)"
RUN wget https://github.com/wiedehopf/tar1090/raw/master/install.sh -O /tmp/install.sh

# Need to create dummy /run files in order for the install to complete
RUN mkdir /run/readsb
RUN touch /run/readsb/aircraft.json
RUN bash /tmp/install.sh

#######################################################################
# Need this for the RTLSDRU
# It has to be installed after dump1090
#######################################################################
WORKDIR /root
RUN git clone https://git.osmocom.org/rtl-sdr.git
WORKDIR /root/rtl-sdr
RUN cmake ./ -DINSTALL_UDEV_RULES=ON
WORKDIR /root/rtl-sdr
RUN make
RUN make install
RUN ldconfig


# Copy root filesystem
COPY rootfs /

COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]