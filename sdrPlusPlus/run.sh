#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"
CONFIG_PATH=/data/options.json

USER="$(bashio::config 'username')"
PASSWORD="$(bashio::config 'password')"


# Start openwebrx


sleep infinity