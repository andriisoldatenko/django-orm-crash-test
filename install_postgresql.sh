#!/bin/bash -ex


if ! command -v psql; then
    echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' > /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    apt-get update
    apt-get install -y postgresql-client-common postgresql-common postgresql-9.6
    apt-get install -y postgresql-9.6-postgis-2.2 pgadmin3 postgresql-contrib-9.6
    cp /vagrant_data/pg_hba.conf /etc/postgresql/9.6/main/
    /etc/init.d/postgresql reload
    createdb -Upostgres pycon
    psql -Upostgres -d pycon -c "CREATE USER pycon_admin WITH PASSWORD 'pycon_admin'"
    psql -Upostgres -d pycon -c "GRANT ALL PRIVILEGES ON DATABASE pycon to pycon_admin"
    psql -Upostgres -d pycon -c "ALTER USER pycon_admin WITH SUPERUSER"
fi

