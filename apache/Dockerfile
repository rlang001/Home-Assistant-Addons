ARG BUILD_FROM=ghcr.io/hassio-addons/base:16.3.6
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# https://github.com/FaserF/hassio-addons/tree/master/apache2


# Create directory for apache2 to store PID file
RUN mkdir /run/apache2

RUN apk --no-cache add apache2 php83-apache2 libxml2-dev apache2-utils apache2-mod-wsgi apache2-ssl
RUN apk --no-cache add php83 php83-dev php83-fpm php83-mysqli php83-opcache php83-gd zlib php83-curl php83-phar php83-mbstring php83-zip php83-pdo php83-pdo_mysql php83-iconv php83-dom php83-session php83-intl php83-soap php83-fileinfo php83-xml php83-ctype php83-pecl-xdebug php83-pdo_sqlite php83-tokenizer php83-exif php83-xmlwriter php83-cgi
RUN apk --no-cache add \
    php83-simplexml \
    php83-gd \
    php83-json \
    php83-imap \
    php83-apcu
RUN apk --no-cache add mosquitto mosquitto-dev
RUN apk --no-cache add mariadb-client
RUN apk --no-cache add ffmpeg

#musl-locales/php-locales
RUN apk add --no-cache cmake make musl-dev gcc gettext-dev libintl
RUN wget https://gitlab.com/rilian-la-te/musl-locales/-/archive/master/musl-locales-master.zip \
    && unzip musl-locales-master.zip \
    && cd musl-locales-master \
    && cmake -DLOCALE_PROFILE=OFF -D CMAKE_INSTALL_PREFIX:PATH=/usr . && make && make install \
    && cd .. && rm -r musl-locales-master

# Install ssh2 extension
#RUN apk --no-cache add libssh2-dev php83-pear zlib-dev build-base
#RUN pecl channel-update pecl.php.net \
#    && pecl install ssh2-1.3.1
#RUN docker-php-ext-enable ssh2
#From here beginning most likely needed
#RUN apk --no-cache add libssh2-dev
#RUN wget -O ssh2.tgz https://pecl.php.net/get/ssh2-1.3.1.tgz \
#    && mkdir ssh2 && tar vxzf ssh2.tgz -C ssh2 --strip-components 1 \
#    && cd ../ssh2 && phpize81 \
#    && ./configure --with-ssh2 --with-php-config=/etc/php83/php.ini \
#    && make && make install \
#    && cd ../ && rm -rf ssh2.tgz ssh2

#Configure Logging
RUN sed -i -r 's@Errorlog .*@Errorlog /dev/stderr@i' /etc/apache2/httpd.conf
RUN echo "Transferlog /dev/stdout" >> /etc/apache2/httpd.conf

# Copy data for add-on
COPY run.sh /
COPY index.html /
RUN chmod a+x /run.sh
RUN chmod a+x /index.html
CMD [ "/run.sh" ]