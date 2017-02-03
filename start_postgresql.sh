#!/usr/bin/env bash
docker run --name postgresql -itd --restart always \
  --publish 5432:5432 \
  --volume /Users/andrii/docker/postgresql:/var/lib/postgresql \
  --env 'DB_USER=university_user' --env 'DB_PASS=university_password' \
  --env 'DB_NAME=university_db' \
  sameersbn/postgresql:9.6

docker exec -it postgresql sudo -u postgres psql -c \
  "GRANT ALL PRIVILEGES ON DATABASE university_db to university_user"
docker exec -it postgresql sudo -u postgres psql -c \
  "ALTER USER university_user WITH SUPERUSER"

PGPASSWORD=university_password psql -q -h localhost -Uuniversity_user -d university_db -t -c \
  "select 'drop table \"' || tablename || '\" cascade;' from pg_tables where tableowner = 'university_user'" |
  PGPASSWORD=university_password psql -h localhost -Uuniversity_user -d university_db