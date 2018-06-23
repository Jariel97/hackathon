#!/usr/bin/env sh

######################################################################
# @author      : Dylan Dsouza (dsouzadyn@gmail.com)
# @file        : clean
# @created     : Saturday Jun 23, 2018 16:14:39 IST
#
# @description : removes the test.db file
######################################################################

rm /tmp/test.db
sleep 3
export export FLASK_APP=app.py
export FLASK_ENV=development
flask run


