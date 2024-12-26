ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
ENV TZ=UTC

RUN apt-get update && apt-get -y upgrade

# Install rsyslog, apache
RUN apt-get install -y software-properties-common wget rsyslog-mysql apache2 mariadb-server cron pip pwgen sqlite3 libdbd-sqlite3 git 

# Tools
RUN apt-get install -y vim procps

# Add the keyring
RUN  sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list' 
RUN wget -qO - https://packages.sury.org/php/apt.gpg | gpg --dearmor | tee /etc/apt/trusted.gpg.d/php7.gpg
RUN apt-get update
# Install PHP.  Loganalyzer only supports up to version 7.x
RUN apt-get install -y php7.2 php7.2-mysql php7.2-gd

# Install loganalyzer
WORKDIR /tmp
RUN wget https://download.adiscon.com/loganalyzer/loganalyzer-4.1.13.tar.gz -O /tmp/loganalyzer.tgz
RUN tar -zxvf /tmp/loganalyzer.tgz 
RUN mv loganalyzer-4.1.13/src/* /var/www/html

WORKDIR /root
RUN wget https://sourceforge.net/projects/libdbi-drivers/files/libdbi-drivers/libdbi-drivers-0.9.0/libdbi-drivers-0.9.0.tar.gz
RUN tar -zxvf libdbi-drivers-0.9.0.tar.gz
WORKDIR libdbi-drivers-0.9.0


#########################################################
# Install MQTT stuff
#########################################################
RUN apt-get install -y python3-paho-mqtt

#########################################################
# have to add the user here before rsyslog is started 
RUN useradd syslog

RUN mkdir /usr/libexec/rsyslog
WORKDIR /usr/libexec/rsyslog 
RUN git clone https://github.com/sohonetlabs/ommqtt
RUN chown -R syslog /usr/libexec/rsyslog
RUN chgrp -R adm /usr/libexec/rsyslog
RUN chmod +x /usr/libexec/rsyslog/ommqtt/ommqtt/ommqtt.py


#########################################################
# Remove apache config
#########################################################
RUN rm -fr \
    /etc/apache2 \
    /etc/rsyslog.conf \
    /etc/rsyslog.d \
    /etc/logrotate.d \
    /var/www/index.html \
    /etc/cron.d \ 
    /etc/cron.daily \
    /etc/cron.hourly \
    /etc/cron.monthly \
    /etc/cron.weekly \
    /etc/cron.yearly \
    /etc/crontab 

#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

#########################################################
# Run the run.sh script
COPY run.sh /
RUN chmod 777 /run.sh
WORKDIR /
CMD [ "/run.sh" ]
