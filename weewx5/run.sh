#!/command/with-contenv bashio
#
###############################################################
set -e

CONFIG_PATH=/data/options.json
RUN_ON_STARTUP="$(bashio::config 'run_on_startup')"
WEEWX_CFG=/config/weewx.conf

# Copy the skin files.  We put them in the config directory so the user can
# make mods that persist through restarts
cp -u -r /root/weewx-data/skins /config

# Copy the station files.  We put them in the config directory so the user can
# make mods that persist through restarts
cp -u -r /root/weewx-data/stations /config

# Copy the default config file if it doesn't exist
cp -u /root/weewx-data/weewx.conf ${WEEWX_CFG}


# Start if the option allows, storing pid
if ${RUN_ON_STARTUP}; then
    bashio::log.info "Starting WeeWX..."
    source ~/weewx-venv/bin/activate; weewxd --config=${WEEWX_CFG} --daemon
fi

sleep infinity




