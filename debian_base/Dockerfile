ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common  vim 


#########################################################
# Copy data for add-on to docker fs
#########################################################
# COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################


COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]




