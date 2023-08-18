#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb;
import sys;


if __name__ == '__main__':
    """the main entry"""
    arguments = sys.argv;
    db = MySQLdb.Connection("localhost", arguments[1], arguments[2], arguments[3]);
    cur = db.cursor();
    ty = cur.execute("SELECT * FROM states");
    lst =cur.fetchall();
    for row in lst:
        print(row);
