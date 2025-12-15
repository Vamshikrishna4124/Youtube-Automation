#!/bin/bash

set -e

echo "Updating apt and installing ffmpeg..."
apt-get update
apt-get install -y ffmpeg

echo "Installing Python dependencies..."
pip install -r /app/requirements.txt

echo "Running daily script..."
python3 /app/python/run_daily.py
