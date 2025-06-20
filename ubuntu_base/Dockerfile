ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

#WORKDIR /tmp
#RUN wget https://github.com/hassio-addons/bashio/archive/refs/tags/v0.16.2.tar.gz 



RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common


#RUN add-apt-repository -y ppa:ondrej/php
#RUN apt-get update -y 
#RUN apt-get install -y php7.4 # php7.4-cli php7.4-fpm # php7.4-mysql



# Fix supervisor
#RUN sed -i '/[supervisord]/a user=root' /etc/supervisor/supervisord.conf
#RUN sed -i 's/[unix_http_server]/[inet_http_server]/g' /etc/supervisor/supervisord.conf
#RUN sed -i 's^file=/var/run/supervisor.sock   ; (the path to the socket file)^port = 127.0.0.1:9001^g' /etc/supervisor/supervisord.conf

#RUN ln -sf /config/syslog /var/log 
# RUN ln -sf /config/syslog/syslog.log /var/log/net/syslog.log 
# RUN chown syslog /var/log/net/syslog.log 

#<<EOF
#if [ -z "$(ls -A /config/syslog 2>/dev/null)" ]; then
#    mkdir -p /config/syslog; 
#fi
#EOF

#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################
# # Create the directory if needed
#RUN sed -i 's/#listen   80;/listen   8099;/g' /etc/nginx/sites-available/default
#RUN sed -i 's;supervisord;i mkdir -p /config/syslog;g' /run.sh


#COPY run.sh /
#RUN chmod 777 /run.sh
#CMD [ "/run.sh" ]




