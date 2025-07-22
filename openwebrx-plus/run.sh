#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"

CONFIG_PATH=/data/options.json

OPENWEBRX_ADMIN_USER="$(bashio::config 'username')"
OPENWEBRX_ADMIN_PASSWORD="$(bashio::config 'password')"



if [ -z "$(ls -A /config/lib 2>/dev/null)" ]; then
    bashio::log.info "Creating default OpenWebRX lib configuration under /config"
    mkdir -p /config/lib
fi
if [ -z "$(ls -A /config/htdocs 2>/dev/null)" ]; then
    bashio::log.info "Creating default OpenWebRX htdocs configuration under /config"
    mkdir -p /config/htdocs
fi

# Copy the settings file if it doesn't exist or is newer
# If /var/lib/openwebrx is not a link
if [ ! -L /var/lib/openwebrx ]; then
    cp -n /var/lib/openwebrx/settings.json /config/lib/settings.json
    cp -n /var/lib/openwebrx/bookmarks.json /config/lib/bookmarks.json
    cp -n /var/lib/openwebrx/users.json /config/lib/users.json
    #cp -n /var/lib/openwebrx/repeaters.json /configlib/repeaters.json

    rm -fr /var/lib/openwebrx
    ln -s /config/lib /var/lib/openwebrx
fi

# Move the htdocs folder 
if [ ! -L /usr/lib/python3/dist-packages/htdocs ]; then
    cp -n -r /usr/lib/python3/dist-packages/htdocs /config
    rm -fr /usr/lib/python3/dist-packages/htdocs
    ln -s /config/htdocs /usr/lib/python3/dist-packages/htdocs
fi

# Set the user/password.  This modifies the /var/lib/openwebrx/users.json file
openwebrx admin --silent hasuser ${OPENWEBRX_ADMIN_USER} || /root/useradmin.exp ${OPENWEBRX_ADMIN_USER} ${OPENWEBRX_ADMIN_PASSWORD}



# Start openwebrx
openwebrx
sleep infinity