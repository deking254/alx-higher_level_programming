#!/usr/bin/python3
import MySQLdb;
import sys;


if __name__ == '__main__':
    """the main entry"""
    arguments = sys.argv;
    db = MySQLdb.Connection("localhost", arguments[1], arguments[2], arguments[3]);
    cur = db.cursor();
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE cities.state_id=states.id ORDER BY cities.id ASC";
    ty = cur.execute(query);
    lst =cur.fetchall();
    for row in lst:
        print(row);
