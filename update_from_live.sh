#!/bin/sh
git pull
cp -r heard ~/webapps/bjp_interactive/
rm -rf ~/webapps/bjp_static/*
mv ~/webapps/bjp_interactive/heard/static/* ~/webapps/bjp_static
cd ~/webapps/bjp_interactive/
./apache2/bin/restart
