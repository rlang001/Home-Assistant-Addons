#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"
CONFIG_PATH=/data/options.json

USER="$(bashio::config 'username')"
PASSWORD="$(bashio::config 'password')"



if [ -z "$(ls -A /config/openwebrx 2>/dev/null)" ]; then
    bashio::log.info "Creating default OpenWebRX configuration under /config/openwebrx"
    mkdir -p /config/openwebrx

    # Copy the settings file if it doesn't exist or is newer
    cp -u /configs/settings.json /config/openwebrx/settings.json
    cp -u /configs/bookmarks.json /config/openwebrx/bookmarks.json
    cp -u /configs/users.json /config/openwebrx/users.json

    bashio::log.info "Please restart"
    exit 0
 i

# These are when /config/openwebrx/ already exists
if [ -z "$(ls -A /config/openwebrx/settings.json 2>/dev/null)" ]; then
    # Copy the settings file if it doesn't exist or is newer
    cp -u /configs/settings.json /config/openwebrx/settings.json
fi

if [ -z "$(ls -A /config/openwebrx/bookmarks.json 2>/dev/null)" ]; then
    cp -u /configs/bookmarks.json /config/openwebrx/bookmarks.json
fi

if [ -z "$(ls -A /config/openwebrx/users.json 2>/dev/null)" ]; then
    cp -u /var/lib/openwebrx/users.json /config/openwebrx/users.json
fi


# Remove the default settings file
rm /var/lib/openwebrx/settings.json
rm /var/lib/openwebrx/bookmarks.json
rm /var/lib/openwebrx/users.json

# Point it to ours
ln -s /config/openwebrx/settings.json /var/lib/openwebrx/settings.json
ln -s /config/openwebrx/bookmarks.json /var/lib/openwebrx/bookmarks.json
ln -s /config/openwebrx/users.json /var/lib/openwebrx/users.json


# Set the user/password.  This modifies the /var/lib/openwebrx/users.json file
/root/useradmin.exp ${USER} ${PASSWORD}


# Start openwebrx
openwebrx


#sleep infinity