FROM jutsuteck/pyjutsu-base:latest

WORKDIR /app

# Copy the Pipfile and Pipfile.lock
COPY --chown=appuser:appuser jutsu-services/auth-service/Pipfile jutsu-services/auth-service/Pipfile.lock /app/

# Copy the other necessary files and directories
COPY --chown=appuser:appuser jutsu-services/auth-service/scripts/startup.sh /app/scripts/
COPY --chown=appuser:appuser jutsu-services/auth-service/alembic /app/alembic
COPY --chown=appuser:appuser jutsu-services/auth-service/alembic.ini /app/
COPY --chown=appuser:appuser jutsu-services/auth-service/src /app/src

# Install the python packages
RUN pipenv install --system --deploy
