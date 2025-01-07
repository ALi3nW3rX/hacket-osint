#!/bin/bash

# Generate the Subfinder configuration file
python3 /app/tools/subfinder/generate_subfinder_config.py

# Run Subfinder with the provided arguments
/go/bin/subfinder "$@"
