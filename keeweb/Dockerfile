ARG BUILD_FROM=keeweb/keeweb:1.19.0
FROM $BUILD_FROM

ENV TZ=UTC

ADD https://github.com/hassio-addons/bashio/archive/v0.15.0.tar.gz  /tmp/bashio.tar.gz
RUN apt-get update && apt-get install -y curl jq && mkdir /tmp/bashio \
    && tar zxvf \
        /tmp/bashio.tar.gz \
        --strip 1 -C /tmp/bashio \
    \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio

