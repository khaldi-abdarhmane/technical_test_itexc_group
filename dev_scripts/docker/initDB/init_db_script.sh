#!/bin/bash

psql -U postgres -c "CREATE USER ${POSTGRES_SIMPLE_USER} PASSWORD '${POSTGRES_SIMPLE_USER_PASSWORD}';"
psql -U postgres -c "CREATE DATABASE ${POSTGRES_DB_NAME} OWNER ${POSTGRES_SIMPLE_USER};"
psql -U postgres -c "CREATE DATABASE ${POSTGRES_DB_UTEST_NAME} OWNER ${POSTGRES_SIMPLE_USER};"