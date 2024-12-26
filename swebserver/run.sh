#!/usr/bin/env bashio
#export PATH="$PATH:/home/weewx/bin"

#CONFIG_PATH=/data/options.json


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

# Create the directory
if [ -z "$(ls -A /config/html 2>/dev/null)" ]; then
    mkdir -p /config/html
fi

# Only copy files that are missing.  Leave user modfied files in place
cp -r -u /home/index.html /config/html


exec nginx
sleep infinity
