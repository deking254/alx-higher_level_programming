#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    quer = "SELECT * FROM states WHERE states.name='{}' ORDER BY states.id ASC"
    ty = cur.execute(quer.format(arg[4]))
    lst = cur.fetchall()
    for row in lst:
        print(row)
