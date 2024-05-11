import http.server as server
import datetime

class TimeHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        current_time = datetime.datetime.now()
        self.send_response(200)
        self.send_header("Connection","Close")
        self.send_header("Content-Type","text/html") 
        self.end_headers()
        self.wfile.write(f"{current_time}".encode("utf-8"))

ss = server.HTTPServer(("0.0.0.0",8005),TimeHandler)
ss.serve_forever()