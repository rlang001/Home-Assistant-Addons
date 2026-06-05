
ARG BUILD_FROM
FROM mjeoffline/viewu:amd64_3.5
     
ARG BASHIO_VERSION="v0.17.5"


ENV TINI_VERSION=v0.19.0
ADD --chmod=0755 https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin
#RUN ["chmod", "+x", "/sbin/tini"]

# RUN curl -J -L -o /tmp/bashio.tar.gz "https://github.com/hassio-addons/bashio/archive/${BASHIO_VERSION}.tar.gz"

#    && mkdir /tmp/bashio \
#    && tar zxvf \
#        /tmp/bashio.tar.gz \
#        --strip 1 -C /tmp/bashio \
#    \
#    && mv /tmp/bashio/lib /usr/lib/bashio \
#    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio 
    
#WORKDIR /app
COPY --chmod=0755 docker-entrypoint.sh /

ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]

#ENTRYPOINT [ "/docker-entrypoint.sh"]
