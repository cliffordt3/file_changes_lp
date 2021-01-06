#!/usr/bin/env python3

import os
import sys
import sqlite3


def getbasefile():
    return os.path.splitext(os.path.basename(__file__))[0]


def connectdb():
    try:
        dbfile = getbasefile() + '.db'
        conn = sqlite3.connect(dbfile, timeout=2)
    except Error as e:
        print("unable to connect to db: {}", e)
    return conn


if __name__ == "__main__":
    c = connectdb()
    print(c.type(c))
