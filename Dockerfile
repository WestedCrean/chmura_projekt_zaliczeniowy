FROM python:3.7

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y netcat-openbsd dos2unix

RUN pip install alembic Click Flask Flask-Login Flask-Migrate Flask-SQLAlchemy itsdangerous Jinja2 Mako MarkupSafe mysqlclient python-dateutil python-dotenv python-editor six SQLAlchemy Werkzeug

COPY . .
RUN dos2unix docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

RUN python3 run.py

CMD ["/bin/bash", "/app/docker-entrypoint.sh"]
