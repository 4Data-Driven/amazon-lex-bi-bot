#!/bin/bash

#
# Creates the Athena database
#

#
# Environment variables to be set in the CodeBuild project
#
# $ATHENA_DB    		    Name of the Athena database
# $ATHENA_BUCKET		    Name of the S3 bucket where the data is stored
# $ATHENA_BUCKET_REGION		Region for the S3 bucket where the data is stored
# $ATHENA_DB_DESCRIPTION	Description for the Athena database
#

echo "Starting build-db.sh"
echo '$ATHENA_DB' "= $ATHENA_DB"
echo '$ATHENA_BUCKET' "= $ATHENA_BUCKET"
echo '$ATHENA_BUCKET_REGION' "= $ATHENA_BUCKET_REGION"
echo '$ATHENA_DB_DESCRIPTION' "= $ATHENA_DB_DESCRIPTION"
echo

# Create 4DATABASE database
echo "Creating Athena database $ATHENA_DB"
aws glue create-database --database-input "Name=$ATHENA_DB,Description=$ATHENA_DB_DESCRIPTION" >/dev/null

# Create 4DATABASE fato table in Athena
echo "Creating fato table..."
aws athena start-query-execution \
    --query-string "create external table fato (serial BIGINT, cod_wave INT, cod_marca INT, cod_det_atribut INT, resposta INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' LOCATION '$ATHENA_BUCKET/fato';" \
    --query-execution-context "Database=$ATHENA_DB" \
    --result-configuration "OutputLocation=$ATHENA_BUCKET/output/" \
    >/dev/null

# Create 4DATABASE marca table in Athena
echo "Creating marca table..."
aws athena start-query-execution \
    --query-string "create external table marca (cod_marca INT, marca STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' LOCATION '$ATHENA_BUCKET/marca';" \
    --query-execution-context "Database=$ATHENA_DB" \
    --result-configuration "OutputLocation=$ATHENA_BUCKET/output/" \
    >/dev/null

# Create 4DATABASE wave table in Athena
echo "Creating wave table..."
aws athena start-query-execution \
    --query-string "create external table wave (cod_wave INT, wave STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' LOCATION '$ATHENA_BUCKET/wave';" \
    --query-execution-context "Database=$ATHENA_DB" \
    --result-configuration "OutputLocation=$ATHENA_BUCKET/output/" \
    >/dev/null

# Create 4DATABASE atributo table in Athena
echo "Creating atributo table..."
aws athena start-query-execution \
    --query-string "create external table atributo (cod_det_atributo INT, det_atributo STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' LOCATION '$ATHENA_BUCKET/atributo';" \
    --query-execution-context "Database=$ATHENA_DB" \
    --result-configuration "OutputLocation=$ATHENA_BUCKET/output/" \
    >/dev/null