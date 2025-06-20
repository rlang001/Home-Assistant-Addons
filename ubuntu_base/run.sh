#!/usr/bin/env bash
#

CONFIG_PATH=/data/options.json
LOG_LEVEL="$(bashio::config 'log_level')"

# Export the http username
if [ -z $SYSLOG_USERNAME ];then
    export SYSLOG_USERNAME=admin
fi

# Export the http password
if [ -z $SYSLOG_PASSWORD ];then
    export SYSLOG_PASSWORD=SyslogP4ss
fi

# Set up the username/password
htpasswd -c -b /etc/nginx/.htpasswd $SYSLOG_USERNAME $SYSLOG_PASSWORD

# Create the user
cd /var/www
php5 -f create-user.php
chown www-data:www-data config.auth.user.php
rm -f create-user.php

# Fix http port for ingress
sed -i 's/#listen   80;/listen   8099;/g' /etc/nginx/sites-available/default

# Create the log directory if needed
mkdir -p /config/syslog

# Create the syslog file if it doesn't exist
if ! [ -e /config/syslog/syslog.log ] ; then 
    touch /config/syslog/syslog.log
fi

# Change the perms
chmod 666 /config/syslog/syslog.log
chown syslog /config/syslog/syslog.log
chgrp adm /config/syslog/syslog.log

# Link the container log file to syslog in /config/syslog
ln -sf /config/syslog/syslog.log /var/log/net/syslog.log 

# Change log directory for syslog
#sed -i 's;WorkDirectory /var/spool/rsyslog;WorkDirectory /config/syslog/rsyslog;g' /etc/rsyslog.conf
#sed -i 's;*.* /var/log/net/syslog.log;*.* /config/syslog/syslog.log;g' /etc/rsyslog.conf

# Fix the log level
#sed -i "s;*.* /var/log/net/syslog.log;*.$LOG_LEVEL /var/log.net/syslog.log;g" /etc/rsyslog.conf
#sed -ir "s;^\*\.w+ ;*.err ;g" /etc/rsyslog.conf

echo $LOG_LEVEL > /log.txt

case $LOG_LEVEL in
    "debug")
        cp -f /root/rsyslog.conf.debug /etc/rsyslog.conf
        echo "debug" >>/log.txt
        ;;

    "info")
        cp -f /root/rsyslog.conf.info /etc/rsyslog.conf
        echo "info" >>/log.txt
        ;;
    
    notice)
        cp -f /root/rsyslog.conf.notice /etc/rsyslog.conf
        ;;
    
    warn)
        cp -f /root/rsyslog.conf.warn /etc/rsyslog.conf
        echo "warn" >>/log.txt
        ;;    
    err)
        cp -f /root/rsyslog.conf.err /etc/rsyslog.conf
        ;;    
    crit)
        cp -f /root/rsyslog.conf.crit /etc/rsyslog.conf
        ;;    
    
    alert)
        cp -f /root/rsyslog.conf.alert /etc/rsyslog.conf
        ;;        
    emerg)
        cp -f /root/rsyslog.conf.emerg /etc/rsyslog.conf
        ;;    
    *)
        cp -f /root/rsyslog.conf /etc/rsyslog.conf
        ;;  
esac

cd
# Run the services
supervisord
~               