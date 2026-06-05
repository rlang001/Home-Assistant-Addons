
ARG BUILD_FROM
FROM mjeoffline/viewu:amd64_0.2.9

ENV TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

WORKDIR /app
COPY rootfs /
ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]

# ENTRYPOINT [ "/docker-entrypoint.sh"]
