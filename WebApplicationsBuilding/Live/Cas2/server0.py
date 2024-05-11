import http.server as server

s = server.HTTPServer(("localhost",8005),server.SimpleHTTPRequestHandler)
s.serve_forever()