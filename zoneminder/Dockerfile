ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC

# Update base packages
RUN apt update \
    && apt upgrade --assume-yes

# Install pre-reqs
# RUN apt install --assume-yes --no-install-recommends gnupg
RUN apt install  --assume-yes --no-install-recommends apache2 mariadb-server php libapache2-mod-php php-mysql lsb-release gnupg2 pwgen


# Configure Zoneminder PPA
RUN curl -s https://zmrepo.zoneminder.com/debian/archive-keyring.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/zmrepo.gpg \
    && apt update

# Install zoneminder
RUN apt install zoneminder --install-recommends -y


RUN chgrp -c www-data /etc/zm/zm.conf 


#########################################################
# Remove configs
#########################################################
RUN rm -fr \
    /etc/apache2



#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /


COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]