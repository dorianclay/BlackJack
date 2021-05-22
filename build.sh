#!/bin/bash

pushd web/blackjack
npm ci
npm run build:prod

rm -rf /usr/share/nginx/html/*
cp dist/blackjack/* /usr/share/nginx/html
popd
