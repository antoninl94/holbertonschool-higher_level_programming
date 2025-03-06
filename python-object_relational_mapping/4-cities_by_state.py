#!/usr/bin/python3
"""
This script list all the cities in the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    conn = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           password=sys.argv[2],
                           database=sys.argv[3],
                           port=3306)

    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
          JOIN states ON states.id = cities.state_id ORDER BY id"
    cur.execute(query)
    cities = cur.fetchall()

    for city in cities:
        print(city)
    cur.close()
    conn.close()
