#!/usr/bin/python3
"""
This script list all states from a database
"""
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="12345",
                        db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states")
    states = cur.fetchall()
    for state in states:
        print(state)
    conn.close()
