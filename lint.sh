#!/bin/bash

bash scripts/install_yapf.sh
bash scripts/run_yapf.sh "${1:--i}"
