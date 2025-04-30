#!/command/with-contenv bashio
#
###############################################################
set -e

CONFIG_PATH=/data/options.json

RUN_ON_STARTUP="$(bashio::config 'run_on_startup')"
WEEWX_CFG=/config/weewx.conf

# Create the html directories for the skin data
# cp -u -r /root/html /config

# Copy the skin files
cp -u -r /root/weewx-data/skins /config



# Copy the default config file if it doesn't exist
cp -u /root/weewx-data/weewx.conf ${WEEWX_CFG}

#echo "$0: Starting WeeWX..."
#source ~/weewx-venv/bin/activate; exec weewxd --config=${WEEWX_CFG} -p /run/weewx.pid


# Start if the option allows, storing pid
if ${RUN_ON_STARTUP}; then
    bashio::log.info "Starting WeeWX..."
    source ~/weewx-venv/bin/activate; weewxd --config=${WEEWX_CFG} --daemon
fi

sleep infinity




