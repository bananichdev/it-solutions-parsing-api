#!/bin/bash

psql -U admin <<-EOSQL
    CREATE DATABASE "it-solutions-parse-db";
EOSQL
