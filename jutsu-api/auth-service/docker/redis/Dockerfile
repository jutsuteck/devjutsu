FROM redis:7.0.11

ARG REDIS_USER
ARG REDIS_PASSWORD

ENV REDIS_USER=${REDIS_USER}
ENV REDIS_PASSWORD=${REDIS_PASSWORD}

COPY docker/redis/redis.conf.template /tmp/redis.conf.template

RUN apt-get update && apt-get install -y gettext && apt-get clean

USER redis

EXPOSE 6379

CMD bash -c "envsubst < /tmp/redis.conf.template > /tmp/redis.conf && exec redis-server /tmp/redis.conf"

