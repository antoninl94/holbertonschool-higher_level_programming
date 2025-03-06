#!/usr/bin/python3
"""
This script list states starting by `N`
"""
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           password=sys.argv[2],
                           database=sys.argv[3],
                           port=3306)

    cur = conn.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name=%s\
        ORDER BY id".format(state_name)
    cur.execute(query, (state_name,))
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    conn.close()
