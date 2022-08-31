#!/bin/sh

function GET_ENV(){
    local param=$1
    echo `cat .env | grep ${param} | cut -d "=" -f 2`
}

read -p "query name {name}.sql ::: " q

PGPASSWORD=`GET_ENV "POSTGRES_PASSWORD"` \
psql --host=`GET_ENV "PG_HOST"` \
     --port=`GET_ENV "PG_PORT"` \
     --username=`GET_ENV "POSTGRES_USER"` \
     --dbname=`GET_ENV "POSTGRES_DB"`<<-EOSQL
`cat ${q}.sql`
EOSQL