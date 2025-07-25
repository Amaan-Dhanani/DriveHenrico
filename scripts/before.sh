#!/bin/bash
set -e

# Ensure config.yml
python ./scripts/ensure-config.py

# Ensure certs
python ./scripts/ensure-certs.py

# Generate caddy file
python ./scripts/generate-caddyfile.py

# Finish