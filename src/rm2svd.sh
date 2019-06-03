#!/usr/bin/env bash
# Compute the singular values on all matrices.

top=$(git rev-parse --show-toplevel)

items=(
    $(gsutil ls -d gs://${BUCKET}/output/mm/5000_5000_add32)
)

for item in ${items[@]}; do
    printf "Processing: %s\n" ${item}
    svd=$(basename ${item})
    gcloud dataproc jobs submit pyspark \
           ${top}/src/spark_svd.py \
           --cluster=${CLUSTER} \
           --region=europe-north1 \
           -- \
           ${item}/* \
           gs://${BUCKET_NAME}/output/svd/${svd}
done
