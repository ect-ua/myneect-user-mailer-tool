#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import psycopg2
from config import *
from user import User
import secrets, sys, csvreader, mailer
import os.path

def connectdb():
    conn_string = "host=%s port=%s dbname=%s user=%s password=%s" % (db_server, db_port, db_name, db_user, db_password)
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    return conn, cur

def closedb():
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python add_users.py <csv file>")
        exit(1)
    
    csv_file = sys.argv[1]
    if not os.path.isfile(csv_file) :
        print("file not found %s" % csv_file)
        exit(2)

    # Reading csv file with the users to add    
    print("Parsing the %s file" % csv_file)
    users = csvreader.read(csv_file)

    # Connecting to the db
    print("Connecting to database")
    conn, cur = connectdb()
    query = "INSERT INTO myneect.new_users (full_name, mail, token) VALUES (%s, %s, %s)"
    print("Adding users...")
    for user in users:
        token = secrets.token_urlsafe(16)
        cur.execute(query, (user.name, user.mail, token))
        conn.commit()
        mailer.send(user.name, user.mail, token)
    closedb()

    print("Done")