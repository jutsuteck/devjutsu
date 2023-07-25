# This Dockerfile is used to build an image for the PostgreSQL database service of the 'jutsu' project.
# 
# Owner: JutsuTeck
# Email: imanuelfebie@devjutsu.io
# 
# This Dockerfile is based on the official PostgreSQL 13 image.
# It installs additional packages necessary for the operation of our specific use case.
# It accepts an ARG for the ENVIRONMENT which can be passed at build time.
# 
# Please reach out to the owner before making significant changes.
#
FROM postgres:13

ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get clean

CMD ["postgres"]

FROM postgres:13

ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get clean

CMD ["postgres"] 
