python3 mavproxy.py --master=/dev/serial0,912600 --aircraft --MyCopter --default-modules "link" --non-interactive &
mavproxy.py --master=/dev/ttyUSB0,115200 --nowait --non-interactive --out=udpbcast:127.0.0.1:14550 &
