# This Dockerfile is used to build an image for the Redis instance of the 'jutsu' project.
# 
# Owner: JutsuTeck
# Email: imanuelfebie@devjutsu.io
# 
# This Dockerfile is based on the Redis 7.0.11 image. It sets up the environment and
# system packages, then installs gettext for environment variable substitution in the 
# Redis configuration file.
# 
# A template configuration file is copied into the image and processed at runtime to 
# substitute the environment variables.
# 
# The Redis server is then started using the processed configuration file.
# 
# Note: The ENVIRONMENT argument can be set at build time to specify the deployment context.
#
# Please reach out to the owner before making significant changes.
#
FROM redis:7.0.11

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

COPY docker/redis/redis.conf.template /tmp/redis.conf.template

RUN apt-get update && apt-get install -y gettext && apt-get clean

USER redis

CMD bash -c "envsubst < /tmp/redis.conf.template > /tmp/redis.conf && exec redis-server /tmp/redis.conf"

