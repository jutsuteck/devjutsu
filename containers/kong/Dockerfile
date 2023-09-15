FROM kong:3.3.1-alpine

COPY containers/kong/kong.yml /etc/kong/kong.yml

ENV KONG_DATABASE=off
ENV KONG_DECLARATIVE_CONFIG=/etc/kong/kong.yml

USER kong
