#!/usr/bin/python3
"""main file"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE BINARY `name` = "{}" ORDER BY
        states.id ASC""".format(sys.argv[4].strip("'")))

    rows = cur.fetchall()
    for row in rows:
        print(row)
