import http.server as server
import datetime 

class HelloHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):   

        query = self.path.split("?")
        param = query[1].split("=")
        name = param[1] 
        
        self.wfile.write(f"HTTP/1.1 200 OK\r\nConnection:close\r\n\r\n".encode("utf-8")) 
        self.wfile.write(f"Hello {name}".encode("utf-8"))

ss = server.HTTPServer(("0.0.0.0",8005),HelloHandler)
ss.serve_forever()
#kucas u url ime, pa ce ti biti izbaceno !!!