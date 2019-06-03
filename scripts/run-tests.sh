#!/usr/bin/env bash
# Run all tests on the cluster.

top=$(git rev-parse --show-toplevel)

for i in $(seq 1 3); do
    ${top}/src/rm2qr.sh
    sleep 120s
done

sleep 180s

for i in $(seq 1 3); do
    ${top}/src/rm2svd.sh
    sleep 120s
done
