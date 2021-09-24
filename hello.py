#!/usr/bin/env python3
import os,json
print("Content-type:text/html\r\n\r\n")
print

print("<title>Test CGI </title>")
print("<p>Hello World</p>")

# 1
# print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)

# 2
for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# 3
for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))