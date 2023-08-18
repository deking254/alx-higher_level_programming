#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    stat = 0
    for ar in arg:
        stat += 1
    if stat == 5:
        quer = "SELECT * FROM states WHERE states.name='{}' "
        y = "ORDER BY states.id ASC"
        query = quer + y
        cur.execute(query.format(arg[4]))
        lst = cur.fetchall()
        for row in lst:
            print(row)
