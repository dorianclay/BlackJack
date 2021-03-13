#!/bin/sh

sh scripts/install_yapf.sh
sh scripts/run_yapf.sh "${1:--i}"
