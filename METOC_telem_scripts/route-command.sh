#!/bin/bash
start_time=$(date +"%T")
$*
printf "Starting telemetry routing\n"
python3 ~/send_telem/mroute.py &
mavlink-routerd -e 127.0.0.1:14550 -e 127.0.0.1:14551 -e 127.0.0.1:14552 /dev/serial0:912600

finish_time=$(date +"%T")

echo "Started at : $start_time"
echo "finished at : $finish_time"

