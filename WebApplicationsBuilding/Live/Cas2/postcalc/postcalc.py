import http.server as server
import urllib.parse as parse

class CalcHandler(server.SimpleHTTPRequestHandler):  
    def do_POST(self): 
        len = int(self.headers["Content-Length"])
        print(len)
        data = self.rfile.read(len).decode("utf-8")
        print(data)
        params = dict(parse.parse_qsl(data))
        print(params)
        res = ""
        if "tb_a" in params and "tb_b" in params: 
            try:
                a = int(params["tb_a"])
                b = int(params["tb_b"])
                ab = a + b
                res = f"Result is {ab}"
            except:
                res = "Parameters must be a valid numbers"
            
        else:
            res = "Parameters missing"

        self.wfile.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close\r\n\r\n") 
        self.wfile.write(f"{res}<hr>".encode("utf-8")) 

ss = server.HTTPServer(("0.0.0.0",8005),CalcHandler)
ss.serve_forever()
