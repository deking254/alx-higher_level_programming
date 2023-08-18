#!/usr/bin/python3
"""SQL Injection handling"""
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    quer = "SELECT * FROM states WHERE states.name=%s "
    y = "ORDER BY states.id ASC"
    query = quer + y
    ty = cur.execute(query, {arg[4]})
    lst = cur.fetchall()
    for row in lst:
        print(row)
