#!/usr/bin/python3
import MySQLdb;
import sys;


if __name__ == '__main__':
    """the main entry"""
    arguments = sys.argv;
    db = MySQLdb.Connection("localhost", arguments[1], arguments[2], arguments[3]);
    cur = db.cursor();
    ty = cur.execute("SELECT * FROM states WHERE states.name='{}' ORDER BY states.id ASC".format(arguments[4]));
    lst =cur.fetchall();
    for row in lst:
        print(row);
