#!/usr/bin/python3
""" script that lists all states with a name starting with N"""
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv;
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    ty = cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    lst =cur.fetchall()
    for row in lst:
        letter = row[1]
        if letter[0] == "N":
            print(row)
