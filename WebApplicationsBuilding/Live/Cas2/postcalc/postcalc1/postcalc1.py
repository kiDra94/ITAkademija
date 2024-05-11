import http.server as server
import urllib.parse as parse

class CalcHandler(server.SimpleHTTPRequestHandler):  
    def do_POST(self): 
        len = int(self.headers["Content-Length"])
        data = self.rfile.read(len).decode("utf-8")
        params = dict(parse.parse_qsl(data))
        print(params)
        res = ""
        if "oper" in params and params["oper"] in ["+","-","*","/"] and "op_a" in params and "op_b" in params:
            try:
                a = int(params["op_a"])
                b = int(params["op_b"]) 
                oper = params["oper"]
                if oper == "+":
                    ab = a + b
                elif oper == "-":
                    ab = a - b
                elif oper == "*":
                    ab = a * b
                else:
                    ab = a / b
                res = f"Result is {ab}"
            except:
                res = "Parameters must be a valid numbers"
            
        else:
            res = "Parameters missing"

        self.wfile.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close\r\n\r\n") 
        self.wfile.write(f"{res}<hr>".encode("utf-8")) 

ss = server.HTTPServer(("0.0.0.0",8005),CalcHandler)
ss.serve_forever()


