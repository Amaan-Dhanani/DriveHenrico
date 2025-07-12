#!/bin/bash
set -e

# Ensure config.yml
python ./scripts/ensure-config.py

# Generate caddy file
python ./scripts/generate-caddyfile.py

# Finish