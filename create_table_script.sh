#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	GRANT ALL PRIVILEGES ON DATABASE faces_measurements TO exploit;
        CREATE TABLE measurements (
  	  id SERIAL PRIMARY KEY,
  	  eye_distance FLOAT NOT NULL,
  	  mouth_shape VARCHAR(10) NOT NULL,
  	  nose_shape VARCHAR(10) NOT NULL,
  	  cheekbone_height FLOAT NOT NULL
	);
EOSQL
