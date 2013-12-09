#!/usr/bin/env python
# coding: utf-8 

import cgi

html_body="""
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
</head>
<body>
String received is %s.
</body>
</html>"""

form = cgi.FieldStorage()
string = form.getfirst('string', 'none').upper()

print "Content-type: text/html;charset=utf-8\n"
print html_body % string

import sqlite3

con = sqlite3.connect('./data.db', isolation_level=None)

con.execute("INSERT INTO val(str) VALUES(?)", [string])
  
cur = con.cursor()
cur.execute("SELECT * from val")

con.close()

