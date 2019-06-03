#!/usr/bin/env bash
# Convert all MatrixMarket files to RDDs on our Google bucket.

top=$(git rev-parse --show-toplevel)

for item in $(gsutil ls gs://${BUCKET}/input/mm/*.mtx); do
    printf "Processing: %s\n" ${item}
    file=$(basename ${item} .mtx)
    gcloud dataproc jobs submit pyspark \
           ${top}/src/matrix_rdd.py \
           --cluster=${CLUSTER} \
           -- \
           ${item} \
           gs://${BUCKET_NAME}/output/mm/${file}
done
