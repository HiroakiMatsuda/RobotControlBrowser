#!/usr/bin/env python
# coding: utf-8 

import sqlite3

con = sqlite3.connect('./data.db', isolation_level=None)

con.execute("""
CREATE TABLE val( 
	id integer primary key autoincrement ,
	str string
);
""")

con.close()


