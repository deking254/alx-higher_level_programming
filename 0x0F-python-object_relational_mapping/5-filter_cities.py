#!/usr/bin/python3
import MySQLdb;
import sys;


if __name__ == '__main__':
    """the main entry"""
    arguments = sys.argv;
    db = MySQLdb.Connection("localhost", arguments[1], arguments[2], arguments[3]);
    cur = db.cursor();
    query = "SELECT cities.name FROM cities JOIN states WHERE cities.state_id=states.id AND states.name=%s ORDER BY cities.id ASC";
    ty = cur.execute(query, {arguments[4]});
    lst =cur.fetchall();
    cities = [];
    status = 0;
    for row in lst:
        cities.append(row[0]);
    print(", ".join(cities));
