#!/usr/bin/python3
import MySQLdb;
import sys;


if __name__ == '__main__':
    """the main entry"""
    arguments = sys.argv;
    db = MySQLdb.Connection("localhost", arguments[1], arguments[2], arguments[3]);
    cur = db.cursor();
    ty = cur.execute("SELECT * FROM states ORDER BY states.id ASC");
    lst =cur.fetchall();
    for row in lst:
        letter = row[1]
        if letter[0] == "N":
            print(row);
