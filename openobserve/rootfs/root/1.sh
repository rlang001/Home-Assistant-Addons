
#!/command/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# Home Assistant Community Add-on: 
# Configures rsyslog
# ==============================================================================
set -e

declare -A mylevel

CONFIG_PATH=/data/options.json

jq '. + {"hostname": `hostname -I`}' /data/options.json > /data/options.json.tmpi
