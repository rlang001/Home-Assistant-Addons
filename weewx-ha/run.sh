#!/usr/bin/env bashio
export PATH="$PATH:/home/weewx/bin"
CONFIG_PATH=/data/options.json

MAINTENANCE_MODE="$(bashio::config 'maintenance_mode')"

if [ -z "$(ls -A /config/weewx 2>/dev/null)" ]; then
    bashio::log.info "Creating default weewx configuration under /config/weewx"
    mkdir -p /config/weewx

    bashio::log.info "Update the /config/weewx/weewx.conf and restart"
    cp -u /home/weewx/weewx.conf /config/weewx/weewx.conf
    exit 0 
fi   


#################################################################
# Copy the skins
#################################################################
## Amphibian
if [ -z "$(ls -A /config/skins/amphibian 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/amphibian
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/amphibian /config/weewx/skins

#################################################################
## Belchertown
if [ -z "$(ls -A /config/skins/Belchertown 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Belchertown
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Belchertown /config/weewx/skins

#################################################################
## neowx-material
if [ -z "$(ls -A /config/skins/neowx-material 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/neowx-material 
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/neowx-material /config/weewx/skins

#################################################################
## neowx-material
if [ -z "$(ls -A /config/weewx/skins/ss 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/ss
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/ss /config/weewx/skins

#################################################################
# NWS
if [ -z "$(ls -A /config/weewx/skins/nws 2>/dev/null)" ]; then
    mkdir -p /config/weewx/nws/Standard
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/nws /config/weewx/skins


#################################################################
## Copy the standard 'skins'
#################################################################
# Ftp
if [ -z "$(ls -A /config/weewx/skins/Ftp 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Ftp
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Ftp /config/weewx/skins

#################################################################
# Mobile
if [ -z "$(ls -A /config/weewx/skins/Mobile 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Mobile
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Mobile /config/weewx/skins

#################################################################
# Rsync
if [ -z "$(ls -A /config/weewx/skins/Rsync 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Rsync
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Rsync /config/weewx/skins

#################################################################
# Seasons
if [ -z "$(ls -A /config/weewx/skins/Seasons 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Seasons
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Seasons /config/weewx/skins

#################################################################
# Smartphone
if [ -z "$(ls -A /config/weewx/skins/Smartphone 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Smartphone
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Smartphone /config/weewx/skins

#################################################################
# Standard
if [ -z "$(ls -A /config/weewx/skins/Standard 2>/dev/null)" ]; then
    mkdir -p /config/weewx/skins/Standard
fi
# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/weewx/skins/Standard /config/weewx/skins


#################################################################
# index.html file
# If it doesn't exist in the /config/weewx directory
if [ -z "$(ls -A /config/weewx/index.html 2>/dev/null)" ]; then
    # Copy the default index.html to the local config directory 
    cp /var/www/html/index.html /config/weewx/index.html
else
    # Copy the user index.html to the NGINX web directory 
    cp /config/weewx/index.html /var/www/html/index.html 
fi


if [[ "${MAINTENANCE_MODE}" = "false" ]]; then
    /home/weewx/bin/weewxd /config/weewx/weewx.conf
else
    bashio::log.info "WARNING! - In maintenance mode."
    bashio::log.info "No weather data will be collected"
    sleep infinity
fi