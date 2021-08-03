#!/bin/bash

pushd web/blackjack
echo ***Setting to CI
sudo npm ci
echo ***Running the production build
sudo npm run build:prod

echo ***Removing existing files
sudo rm -rf /usr/share/nginx/html/*
echo ***Copying new files
sudo cp -r dist/blackjack/* /usr/share/nginx/html
popd
