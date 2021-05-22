#!/bin/bash

sudo cp blackjack.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start blackjack.service
sudo apt install nginx
sudo cp blackjack.conf /etc/nginx/conf.d

