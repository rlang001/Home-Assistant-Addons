#!/usr/bin/env bashio
#export PATH="$PATH:/home/weewx/bin"

#CONFIG_PATH=/data/options.json



# line copied from /etc/init.d/apache2
#ENV="env -i LANG=C PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV="env -i LANG=C PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/dump1090"


# Generate Ingress configuration
bashio::var.json \
    interface "$(bashio::addon.ip_address)" \
    | tempio \
        -template /etc/nginx/templates/ingress.gtpl \
        -out /etc/nginx/servers/ingress.conf
    
# Generate direct access configuration, if enabled.
#if bashio::var.has_value "$(bashio::addon.port 80)"; then
    tempio \
        -template /etc/nginx/templates/direct.gtpl \
        -out /etc/nginx/servers/direct.conf
#fi  



exec /usr/bin/readsb --device-type rtlsdr --json-location-accuracy 2 --range-outline-hours 24 --device 1 --net --write-json /run/readsb --tar1090-use-api &
exec nginx

sleep infinity
