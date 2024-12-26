#!/usr/bin/env bashio
export PATH="$PATH:/usr/local/bin"
CONFIG_PATH=/data/options.json

export LD_LIBRARY_PATH=/usr/local/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}


#IP="$(hostname -I)"
#DEVICE="$(bashio::config 'device')"
#FREQUENCY="$(bashio::config 'frequency')"
#GAIN="$(bashio::config 'gain')"
#SAMPLERATE="$(bashio::config 'samplerate')"
#BUFFERS="$(bashio::config 'buffers')"

exec rtl_rcp -d 1

#exec rtl_tcp -a ${IP} \
#    -d ${DEVICE} \
#    -f ${FREQUENCY}
#    -g ${GAIN} \
#    -s ${SAMPLERATE} \
#    -b ${BUFFERS}

sleep infinity