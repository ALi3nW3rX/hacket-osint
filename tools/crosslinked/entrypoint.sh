#!/bin/bash
mkdir -p /app/output
python3 crosslinked.py "$@"
mv names.csv /app/output/names.csv
mv names.txt /app/output/names.txt

