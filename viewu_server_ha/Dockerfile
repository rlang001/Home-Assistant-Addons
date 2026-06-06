
ARG BUILD_FROM
FROM mjeoffline/viewu:amd64_3.5
     
ARG BASHIO_VERSION="v0.17.5"

# Source - https://stackoverflow.com/a/71756170
# Posted by aoee, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-06, License - CC BY-SA 4.0

FROM busybox:1.35.0-uclibc as busybox
FROM gcr.io/distroless/base-debian11

# Now copy the static shell into base image.
COPY --from=busybox /bin/sh /bin/sh

# You may also copy all necessary executables into distroless image.
COPY --from=busybox /bin/mkdir /bin/mkdir
COPY --from=busybox /bin/cat /bin/cat

#ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]


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
