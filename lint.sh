#!/bin/bash

find . -type f -name "*.py" | xargs yapf --style="google" "${1:--i}"