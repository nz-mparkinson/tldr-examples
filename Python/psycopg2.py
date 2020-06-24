#!/usr/bin/python

#Python setup
#sudo pip install psycopg2

#Import libraries
import psycopg2



try:
    conn = psycopg2.connect(host = "192.168.122.218", database = "test", user = "postgres", password = "postgres")
    cur = conn.cursor()
    cur.execute("""SELECT datname from pg_database""")
    print("\nShow me the databases:\n")
    for row in rows:
        print("   ", row[0])
except:
    print("I am unable to connect to the database")



