#!/bin/sh

container_name=mock

function GET_ENV(){
    local param=$1
    echo `cat .env | grep ${param} | cut -d "=" -f 2`
}

function START_PSQL_CONTAINER(){
    docker run -d \
        --name ${container_name} \
        -p `GET_ENV "PG_PORT"`:5432 \
        -e POSTGRES_PASSWORD=`GET_ENV "POSTGRES_PASSWORD"` \
        -e POSTGRES_USER=`GET_ENV "POSTGRES_USER"` \
        -e POSTGRES_DB=`GET_ENV "POSTGRES_DB"` \
        -v `pwd`/mount:/var/lib/postgresql/data \
        postgres
}


# docker image check
dockerImages=`docker image ls | grep postgres`

if [[ ${dockerImages} != *${container_name}* ]]
then
    echo "!!! Postgres docker image is not exist. !!!"
    echo "==> Now Start postgres docker image download from docker hub."
    docker pull postgres
else
    echo "!!! Docker image already existed. !!!"
    echo "==> Docker image pulling is skiped"
fi

# docker container check
dockerPsA=`docker ps -a | grep ${container_name}`

if [[ ${dockerPsA} != *${container_name}* ]]
then
    echo "!!! ${container_name} docker container is not exist. !!!"
    echo "==> Now Start postgres docker container at local for mocking DB."
    
    START_PSQL_CONTAINER
   
elif [[ ${dockerPsA} == *${container_name}* ]]
then
    echo "!!! Docker container already existed. !!!"
    
    echo "==> Do you want to remove and build again? [y/n]"
    read ans
    if [[ ${ans} == "y" ]]
    then
        docker rm -f ${container_name}
        echo "==> Existed container is removed"
        START_PSQL_CONTAINER

    elif [[ ${ans} == "n" ]]
    then
        echo "==> Existed container is starting"
        docker start ${container_name}
    else
        echo "Invalid answer :^("
    fi
fi


echo "::::: psql head :::::"

PGPASSWORD=`GET_ENV "POSTGRES_PASSWORD"` \
psql --host=`GET_ENV "PG_HOST"` \
     --port=`GET_ENV "PG_PORT"` \
     --username=`GET_ENV "POSTGRES_USER"` \
     --dbname=`GET_ENV "POSTGRES_DB"` <<-EOSQL
SELECT 1;
EOSQL

EXISTED_STATUS = $?
if [[ ${EXISTED_STATUS} -eq 0 ]]
then
    echo "All script is done"
else
    echo "something wrong;;"