#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import socket
import time
import os
import psql.db
import datetime

if __name__ == '__main__':
    
    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    DBNAME = os.environ.get('DBNAME')
    DBHOST = os.environ.get('DBHOST')

    if not DBHOST:
        DBHOST="127.0.0.1"
    DBPORT = os.environ.get('DBPORT')
    if not DBPORT:
        DBPORT=str(5432)

    print(time.asctime(),"pingdb: Initiating connection to DB")
    db_session = psql.db.db(user=DBUSER, password=DBPASS,host=DBHOST,database=DBNAME)

    db_session.close_db()