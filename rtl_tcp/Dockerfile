ARG BUILD_FROM
FROM $BUILD_FROM

LABEL \
    io.hass.version="VERSION" \
    io.hass.type="addon" \
    io.hass.arch="armhf|aarch64|i386|amd64"

# Install requirements for add-on
#RUN apk add --no-cache example_alpine_package

# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

#########################################################
COPY rootfs /

#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]
