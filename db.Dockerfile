FROM postgres:12

COPY create_table_script.sh /docker-entrypoint-initdb.d/

RUN chmod 777 /docker-entrypoint-initdb.d/create_table_script.sh

#RUN psql -h localhost -p 5432 -U exploit -d faces_measurements -f /docker-entrypoint-initdb.d/create_database_script.sql

CMD ["postgres"]
