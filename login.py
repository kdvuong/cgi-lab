#!/usr/bin/env python3
import cgi
from secret import username, password
from templates import secret_page, after_login_incorrect
form = cgi.FieldStorage()

input_username = form.getvalue("username")
input_password = form.getvalue("password")

if input_username == username and input_password == password:
    print("Set-Cookie:UserId = %s;\r\nSet-Cookie:Password = %s;\r\nContent-Type:text/html\r\n\r\n" % (username,password))
    print(secret_page(username, password))  
else:
    print(after_login_incorrect())
