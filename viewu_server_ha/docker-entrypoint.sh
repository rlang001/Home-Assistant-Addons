
#!/usr/bin/env bashio

#bashio::log.info "Preparing to start..."

# Check if HA supervisor started
# Workaround for:
# - https://github.com/home-assistant/supervisor/issues/3884
# - https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/issues/387
# bashio::config.require 'data_path'

#function export_config() {
#    local key=${1}
#    local subkey

#    if bashio::config.is_empty "${key}"; then
#        return
#    fi

#    for subkey in $(bashio::jq "$(bashio::config "${key}")" 'keys[]'); do
#        export "MQTT_$(bashio::string.upper "${key}")_$(bashio::string.upper "${subkey}")=$(bashio::config "${key}.${subkey}")"
#    done
#}

#export_config 'mqtt'

#if bashio::config.is_empty 'mqtt' && bashio::var.has_value "$(bashio::services 'mqtt')"; then
#    if bashio::var.true "$(bashio::services 'mqtt' 'ssl')"; then
#        export MQTT_IP="mqtts://$(bashio::services 'mqtt' 'host')"
#    else
#        export MQTT_IP="mqtt://$(bashio::services 'mqtt' 'host')"
#    fi
#    export MQTT_PORT="$(bashio::services 'mqtt' 'port')"
#    export MQTT_USER="$(bashio::services 'mqtt' 'user')"
#    export MQTT_PASSWORD="$(bashio::services 'mqtt' 'password')"
#fi

#bashio::log.info "Starting Viewu Server..."
cd /usr/local/bin/

export MQTT_IP="192.168.10.9"
export MQTT_PORT="1883"
export MQTT_USER="mqtt"
export MQTT_PASSWORD="Sadi3Bail33"

#exec sh -c viewu_server $MQTT_SERVER $MQTT_PORT $MQTT_USER $MQTT_PASSWORD
# exec sh -c viewu_server "192.168.10.9" 1883 "mqtt" "Sadi3Bail33"
exec sh

