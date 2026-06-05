
ARG BUILD_FROM
FROM mjeoffline/viewu:amd64_0.2.9

WORKDIR /app
COPY rootfs /
# ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]

COPY run.sh /
RUN chmod 777 /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh"]
