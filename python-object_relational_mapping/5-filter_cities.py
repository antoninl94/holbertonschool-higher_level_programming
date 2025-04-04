#!/usr/bin/python3
"""
This script takes in the name of a state as an
argument and lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    conn = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           password=sys.argv[2],
                           database=sys.argv[3],
                           port=3306)

    cur = conn.cursor()
    query = "SELECT cities.name FROM cities\
        JOIN states ON states.id = cities.state_id WHERE states.name=%s\
            ORDER BY cities.id"
    state=sys.argv[4]
    cur.execute(query, (state,))
    cities = cur.fetchall()
    count = 0
    for city in cities:
        if count != 0:
            print(',', end=' ')
        print(city[0], end='')
        count += 1
    print()
    cur.close()
    conn.close()
