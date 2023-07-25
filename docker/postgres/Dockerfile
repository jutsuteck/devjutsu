FROM postgres:13

# Define the environment
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get clean

CMD ["postgres"] 
