#!/bin/bash

DIR=$(dirname "${BASH_SOURCE[0]}")
source "${DIR}/paths.rc"

find . -type f -name "*.py" ! -path "./${YAPF_TARGET}/*" | xargs yapf-files/bin/yapf --style="google" "$1"