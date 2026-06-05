
ARG BUILD_FROM
FROM mjeoffline/viewu:amd64_3.5
     

ENV TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin
RUN chmod +x /sbin/tini

#WORKDIR /app
COPY --chmod=0755 docker-entrypoint.sh /

ENTRYPOINT [ "/sbin/tini", "--", "/docker-entrypoint.sh"]

#ENTRYPOINT [ "/docker-entrypoint.sh"]
