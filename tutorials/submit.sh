#!/usr/bin/env sh
top=$(git rev-parse --show-toplevel)
gcloud dataproc jobs submit pyspark ${top}/tutorials/wordcount.py --cluster=${CLUSTER} -- gs://${BUCKET_NAME}/input/txt/rose.txt gs://${BUCKET_NAME}/output/txt
gsutil cat gs://${BUCKET}/output/txt/*
