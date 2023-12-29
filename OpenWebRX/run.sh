#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"
CONFIG_PATH=/data/options.json


if [ -z "$(ls -A /config/openwebrx 2>/dev/null)" ]; then
    bashio::log.info "Creating default OpenWebRX configuration under /config/openwebrx"
    mkdir -p /config/openwebrx

    bashio::log.info "Update the /config/openwebrx/weewx.conf and restart"
    cp -u /etc/openwebrx/openwebrx.conf /config/openwebrx/openwebrx.conf
    rm -f /config/openwebrx/openwebrx.conf
    ln -s /config/openwebrx/openwebrx.conf /etc/openwebrx/openwebrx.conf 
    exit 0 
fi   

# Remove the default settings file
rm /var/lib/openwebrx/settings.json
rm /var/lib/openwebrx/bookmarks.json
rm /var/lib/openwebrx/users.json

# Point it to ours
ln -s /config/openwebrx/settings.json /var/lib/openwebrx/settings.json
ln -s /config/openwebrx/bookmarks.json /var/lib/openwebrx/bookmarks.json
ln -s /config/openwebrx/users.json /var/lib/openwebrx/users.json

# Start openwebrx
openwebrx

#sleep infinity