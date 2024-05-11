import http.server as server
import datetime

class TimeHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        current_time = datetime.datetime.now()
        print(current_time)
        self.wfile.write(f"HTTP/1.1 200 OK\r\nConnection:close\r\n\r\n".encode("utf-8")) 
        self.wfile.write(f"{current_time}".encode("utf-8"))

ss = server.HTTPServer(("0.0.0.0",8005),TimeHandler)
ss.serve_forever()
#gasi server u terminalu sa ctrl+C