

build_from:
  # aarch64: mjeoffline/viewu:arm64
  amd64: mjeoffline/viewu:amd64_0.2.9

ARG BUILD_FROM
FROM $BUILD_FROM  

WORKDIR /app
COPY rootfs /
ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]

