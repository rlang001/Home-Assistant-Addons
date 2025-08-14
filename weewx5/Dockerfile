ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

#ENV WEEWX_ROOT=/etc/weewx
ENV WEECTL="weectl"
#ENV DEFAULT_CONFIG_FILE="/root/weewx-temp.conf"
ENV INITIAL_CONFIG_FILE="/root/weewx-data/weewx.conf"
#ENV MQTTSUBSCRIBE_VERSION="2.3.1"
ENV MQTTSUBSCRIBE_VERSION="3.0.0"
ENV NWS_VERSION="4.5.5"
# Needed for MQTTSubscribe service 
ENV RUN_MODE="driver"          

# Install base system
RUN apt-get update && apt-get upgrade -y && \ 
    apt-get install -y software-properties-common wget gnupg sqlite3 unzip rtl-sdr rtl-433 nginx vim procps \
        xtide python3.8 python3-pip python3.8-venv

WORKDIR /root

### Weewx ###########################
# #### Install WeeWX and extensions into the virtual environment
# 1. Create the python venv
# 2. Install WeeWX
# 3. Install addons
# 4. Create the weewx.conf - Don't set HTML_ROOT here
# 5. Install extensions


# Download/unzip some skins
# Create the python venv
# Install WeeWX, pyserial requests, paho-mqtt, and python-dateutil
RUN wget -O "/tmp/weewx-wdc.zip" https://github.com/Daveiano/weewx-wdc/releases/download/v3.5.1/weewx-wdc-v3.5.1.zip && \
    wget -O "/tmp/weewx-jas.zip" https://github.com/bellrichm/weewx-jas/archive/refs/tags/v1.1.1.zip && \
    wget -O "/tmp/weewx-forecast.zip" https://github.com/chaunceygardiner/weewx-forecast/releases/download/v3.5/weewx-forecast-3.5.zip && \
    \    
    mkdir /tmp/weewx-wdc/ && \
    unzip /tmp/weewx-wdc.zip -d /tmp/weewx-wdc/ && \
    unzip /tmp/weewx-jas.zip -d /tmp && \
    \
    python3 -m venv ~/weewx-venv && \
    source ~/weewx-venv/bin/activate && \
    python3 -m pip install weewx && \
    pip3 install pyserial requests && \
    pip3 install paho-mqtt && \
    pip3 install python-dateutil
    
# Copy our database extension schema to the virtual env
COPY /data/weewx-data/wview_extended.py /root/weewx-venv/lib/python3.8/site-packages/schemas

# 
# Create the weewx.conf using default data
# Install some extensions
RUN source ~/weewx-venv/bin/activate && \
    weectl station create --no-prompt --driver=weewx.drivers.simulator --location="My Station" \
        --altitude="0, foot" --latitude=40.7129822 --longitude=-74.007205  \
        --register=n --units=us  --skin-root=/root/weewx-data/skins \
        --user-root=/root/weewx-data/bin/user --config=/root/weewx-data/weewx.conf && \
    \
    weectl extension install https://github.com/matthewwall/weewx-sdr/archive/master.zip --config=${INITIAL_CONFIG_FILE} -y  && \
    weectl extension install https://github.com/matthewwall/weewx-mqtt/archive/master.zip --config=${INITIAL_CONFIG_FILE} -y  && \
    weectl extension install https://github.com/bellrichm/WeeWX-MQTTSubscribe/archive/refs/tags/v${MQTTSUBSCRIBE_VERSION}.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/chaunceygardiner/weewx-nws/releases/download/v${NWS_VERSION}/weewx-nws.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/poblabs/weewx-belchertown/releases/download/weewx-belchertown-1.3.1/weewx-belchertown-release.1.3.1.tar.gz --config=${INITIAL_CONFIG_FILE} -y  && \
    weectl extension install https://neoground.com/neowx-material/download/latest --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/matthewwall/weewx-amphibian/archive/master.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/matthewwall/weewx-simple/archive/master.zip  --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/bourquep/weewx-me.teo/releases/latest/download/weewx-me.teo.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install https://github.com/matthewwall/weewx-cmon/archive/refs/heads/master.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install  https://github.com/roe-dl/weewx-DWD/archive/master.zip --config=${INITIAL_CONFIG_FILE} -y && \
    weectl extension install /tmp/weewx-wdc/ --config=${INITIAL_CONFIG_FILE} -y  && \
    weectl extension install /tmp/weewx-forecast.zip --config=${INITIAL_CONFIG_FILE} -y && \
    cp /tmp/weewx-jas-1.1.1/bin/user/jas.py /root/weewx-data/bin/user && \ 
    cp -r /tmp/weewx-jas-1.1.1/skins/* /root/weewx-data/skins

    #weectl extension install /tmp/forecast.zip --config=${INITIAL_CONFIG_FILE} -y && \

    #weectl extension install https://github.com/matthewwall/weewx-forecast/archive/master.zip --config=${INITIAL_CONFIG_FILE} -y && \
    #weectl extension install https://github.com/brewster76/fuzzy-archer/archive/refs/heads/master.zip --config=${INITIAL_CONFIG_FILE} -y
    #weectl extension install https://github.com/stormchasertech/obwx/archive/main.zip --config=${INITIAL_CONFIG_FILE} -y
    #weectl extension install https://github.com/bourquep/weewx-me.teo/releases/latest/download/weewx-me.teo.zip --config=${INITIAL_CONFIG_FILE} -y && \
    #weectl extension install https://github.com/glennmckechnie/alltimeSeasons/archive/refs/heads/master.zip --config=${INITIAL_CONFIG_FILE} -y

########################################################################
# Copy the conf files 
# Fix up the weewx.conf file
#   1. Add the logging section as we are not using syslog
#   2. Set the HTML_ROOT to the Standard directory so as not to overwrite our pages
#   3. Set the skins html roots
#   4. Point the database directories to /config
#   5. Remove the StdPrint service (it is really chatty)
#   6. Add the entry for NeoWX-material 
#
COPY /data/weewx-data/logging.conf /root/weewx-data/logging.conf
COPY /data/weewx-data/neowx-material.conf /root/weewx-data/neowx-material.conf
COPY /data/weewx-data/jas.conf /root/weewx-data/jas.conf
COPY /data/weewx-data/sdr.conf /root/weewx-data/sdr.conf
COPY /data/weewx-data/extensions.py /root/weewx-data/extensions.py
COPY /data/fixup.py /root/fixup.py

COPY /data/weewx-data/stations /root/weewx-data/stations

RUN source ~/weewx-venv/bin/activate && \
    python3 /root/fixup.py

#########################################################
# Remove nginx config, temp stuff
#########################################################
RUN rm -fr \
/etc/nginx \
/var/www/html \
/tmp/*


#########################################################
# Copy data for add-on to docker 
#########################################################
COPY rootfs /


# WeeWX and NGinx are started by the s6-overlay

########################################################
# Modify the existing /run.sh file
########################################################
#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]



