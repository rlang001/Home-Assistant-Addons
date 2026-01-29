ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

RUN apk add --no-cache --update 

#########################################################
# Copy data for add-on to docker fs
#########################################################
#COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################


COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]




