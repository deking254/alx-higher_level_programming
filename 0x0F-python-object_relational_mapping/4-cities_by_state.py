#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    quer = "SELECT cities.id, cities.name, states.name FROM cities JOIN "
    y = "states WHERE cities.state_id=states.id ORDER BY cities.id ASC"
    query = quer + y
    ty = cur.execute(query)
    lst = cur.fetchall()
    for row in lst:
        print(row)
