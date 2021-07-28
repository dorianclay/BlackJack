#!/bin/bash

echo *** Copying the blackjack service...
sudo cp blackjack.service /etc/systemd/system

echo *** Reloading daemons...
sudo systemctl daemon-reload
sudo systemctl start blackjack.service

echo *** Copying ngnix configuration...
sudo apt install nginx
sudo cp blackjack.conf /etc/nginx/conf.d

echo *** Done, all set.

