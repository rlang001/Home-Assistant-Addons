#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"

export LD_LIBRARY_PATH=/usr/local/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}


CONFIG_PATH=/data/options.json

DEVICE="$(bashio::config 'device')"
FREQUENCY="$(bashio::config 'frequency')"
GAIN="$(bashio::config 'gain')"
SAMPLERATE="$(bashio::config 'samplerate')"
BUFFERS="$(bashio::config 'buffers')"

#exec rtl_tcp -a 172.30.33.11 \
#    -d ${DEVICE} \
#    -f ${FREQUENCY}
#    -g ${GAIN} \
#    -s ${SAMPLERATE} \
#    -b ${BUFFERS}


sleep infinity