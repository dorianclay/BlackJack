#!/bin/sh

DIR=$(dirname "${BASH_SOURCE[0]}")
source "${DIR}/paths.rc"

if [ ! -e "$YAPF_TARGET" ]; then
  pip3 install --target "$YAPF_TARGET" yapf
fi
