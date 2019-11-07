#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create table IF NOT EXISTS public.logmessages (
    id serial primary key,
    date timestamp default null,
    logmessage varchar(4000) not null);
    commit;
EOSQL