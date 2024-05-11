import http.server as server
import datetime

class CalcHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):  
        query = self.path.split("?")
        params = {}
        if len(query)>1:
            query = query[1] 
            p1 = query.split("&")
            for param in p1:
                p2 = param.split("=")
                if len(p2)>1:
                    params[p2[0]] = p2[1] 
        
        res = 'No params or params not valid'
        if 'a' in params and 'b' in params:
            try:
                r = int(params['a']) + int(params['b'])
                res = f"Result is : {r}"
            except:
                pass 

        self.wfile.write(f"HTTP/1.1 200 OK\r\nConnection:close\r\n\r\n".encode("utf-8")) 
        self.wfile.write(res.encode("utf-8"))

ss = server.HTTPServer(("0.0.0.0",8005),CalcHandler)
ss.serve_forever()
#kucas u url ime, pa ce ti biti izbaceno !!!