FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
COPY create-fixtures.sql /docker-entrypoint-initdb.d/create-fixtures.sql
