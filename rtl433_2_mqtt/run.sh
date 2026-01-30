#!/usr/bin/env bashio
#
declare -a options

CONFIG_PATH=/data/options.json

cp --update=none /root/config.yaml /config

## Copy the config files if they don't exist
# cp -n /root/rtl_433.sdr0.conf /config
cp /root/rtl_433_sdr+exmaple.conf /config

cp --update=none /root/rtl_433_sdr0.conf /config

# cp -n /root/rtl_433.sdr1.conf /config
cp --update=none /root/rtl_433_sdr1.conf /config

# cp -n /root/rtl_433.sdr2.conf /config
cp --update=none /root/rtl_433_sdr2.conf /config

# Get the options

# SDR
SDR0_ENABLE=$(bashio::config 'sdr0_enable')
SDR0_CONFIG=$(bashio::config 'rtl_433_sdr0_conf_file')

SDR1_ENABLE=$(bashio::config 'sdr1_enable')
SDR1_CONFIG=$(bashio::config 'rtl_433_sdr1_conf_file')

SDR2_ENABLE=$(bashio::config 'sdr2_enable')
SDR2_CONFIG=$(bashio::config 'rtl_433_sdr2_conf_file')

# Auto discovery
HA_DISCOVERY=$(bashio::config 'ha_discovery')
DISCOVERY_LOG_LEVEL=$(bashio::config 'discovery_log_level')


if ${SDR0_ENABLE}; then
    bashio::log.info "Starting SDR0 using /config/"${SDR0_CONFIG}
    exec /usr/bin/rtl_433 -c "/config/"${SDR0_CONFIG} &
fi

if ${SDR1_ENABLE}; then
    bashio::log.info "Starting SDR1 using /config/"${SDR1_CONFIG}
    exec /usr/bin/rtl_433 -c "/config/"${SDR1_CONFIG} & 
fi

if ${SDR2_ENABLE}; then
    bashio::log.info "Starting SDR2 using /config/"${SDR2_CONFIG}
    exec /usr/bin/rtl_433 -c "/config/"${SDR2_CONFIG} &
fi


if ${HA_DISCOVERY}; then
    bashio::log.info "Starting Home Assistant discovery..."
    python3 -u /root/rtl_433_mqtt_hass.py -l ${DISCOVERY_LOG_LEVEL} & 
fi

sleep infinity
