#!/bin/bash
source /home/ubuntu/Music-cost/venv/bin/activate

cd "$(dirname "$0")"

echo "Generating report..."
python3 generate_report.py

echo "Sending email..."
python3 send_email.py