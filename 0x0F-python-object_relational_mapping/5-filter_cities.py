#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities """
import MySQLdb
import sys


if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.Connection("localhost", arg[1], arg[2], arg[3])
    cur = db.cursor()
    quer = "SELECT cities.name FROM cities JOIN states WHERE "
    y = "cities.state_id=states.id AND states.name=%s ORDER BY cities.id ASC"
    query = quer + y
    ty = cur.execute(query, {arg[4]})
    lst = cur.fetchall()
    cities = []
    status = 0
    for row in lst:
        cities.append(row[0])
    print(", ".join(cities))
