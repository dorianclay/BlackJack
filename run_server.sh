#! /bin/bash

python3 gun.py -k flask_sockets.worker -b 0.0.0.0:5000 --chdir server app:app
