#!/usr/bin/env python3
import sys
import os
import json

port = json.loads(os.environ['wsb.config'])['server_port2']
port = '' if port == 80 else ':' + str(port)
sys.stdout.buffer.write("""Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Test Capture Frame</title>
</head>
<body>
<object data="//localhost{port}/capture_object2/frames/frame1.html" width="200" height="200">frame1.html</object>
<object data="//localhost{port}/capture_object2/frames/frame2.xhtml" width="200" height="200">frame2.xhtml</object>
<object data="//localhost{port}/capture_object2/frames/frame3.svg" width="200" height="200">frame3.svg</object>
<object data="//localhost{port}/capture_object2/frames/frame4.txt" width="200" height="200">frame4.txt</object>
</body>
</html>""".format(port=port).encode("UTF-8"))
