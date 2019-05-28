#!/usr/bin/env bash
# Compute the singular values on all matrices.

top=$(git rev-parse --show-toplevel)

for item in \
    $(gsutil ls -d gs://${BUCKET}/output/mm/10_*) \
        $(gsutil ls -d gs://${BUCKET}/output/mm/100_*) \
        $(gsutil ls -d gs://${BUCKET}/output/mm/1000_*) \
        $(gsutil ls -d gs://${BUCKET}/output/mm/10000_*) \
    ;
do
    printf "Processing: %s\n" ${item}
    svd=$(basename ${item})
    gcloud dataproc jobs submit pyspark \
           ${top}/src/spark_svd.py \
           --cluster=${CLUSTER} \
           -- \
           ${item}/* \
           gs://${BUCKET_NAME}/output/svd/${svd}
done
