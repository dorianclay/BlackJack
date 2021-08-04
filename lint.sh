#!/bin/bash

os="$(uname -s)"
case "${os}" in
    Darwin*)    
        find . -type f -name "*.py" | xargs python3 -m yapf --style="google" "${1:--i}";;
    
    *)     
        find . -type f -name "*.py" | xargs yapf --style="google" "${1:--i}";;
esac
