ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app
COPY rootfs /
# ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]
ENTRYPOINT [ "/docker-entrypoint.sh"]
