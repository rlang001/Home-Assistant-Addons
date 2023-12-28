#!/usr/bin/env bashio
#export PATH="$PATH:/home/weewx/bin"

#CONFIG_PATH=/data/options.json



# line copied from /etc/init.d/apache2
#ENV="env -i LANG=C PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV="env -i LANG=C PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/dump1090"

bashio::log.info "Starting dump1090"
cd /root/dump1090
./dump1090 --interactive --net --net-http-port 5280

#sleep infinity
