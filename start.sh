#!/bin/bash

# Install FFmpeg
apt-get update
apt-get install -y ffmpeg

# Install Python dependencies
pip install -r requirements.txt

# Run the main script
python3 python/run_daily.py
