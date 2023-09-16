FROM kong:latest

COPY containers/kong/kong.yml /etc/kong/kong.yml

ENV KONG_DATABASE=off
ENV KONG_DECLARATIVE_CONFIG=/etc/kong/kong.yml

USER kong
