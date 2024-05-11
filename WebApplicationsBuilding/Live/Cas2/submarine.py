import http.server as server
import random

class SubmarineHandler(server.SimpleHTTPRequestHandler):
    def parse_params(self):
        x = -1
        y = -1
        query = self.path.split("?")
        params = {}
        if len(query)>1:
            query = query[1] 
            p1 = query.split("&")
            for param in p1:
                p2 = param.split("=")
                if len(p2)>1:
                    params[p2[0]] = p2[1]  
        if 'x' in params and 'y' in params:
            try:
                x = int(params['x'])
                y = int(params['y']) 
            except:
                pass 
        return x,y

    def comp_pick(self):
        coords = [] 
        for i in range(10):
            while True:
                record = random.sample(range(0,10),2) 
                if record not in coords:
                    coords.append(record)
                    break
        return coords

    def draw_grid(self,px,py,comp):
        res = ""
        for y in range(10):
            for x in range(10):
                color = "yellow"
                isComp = False
                if [x,y] in comp:
                    isComp = True
                    color = "blue"
                if x == px and y == py:
                    color = "green" if isComp else "red"
                        

                res+=f"<div style='margin:1px;width:30px;height:30px;float:left;background-color:{color};'></div>"
            res+="<div style='clear:both;'></div>" 

        self.wfile.write(res.encode("utf-8"))

    def do_GET(self):   
        x,y = self.parse_params()
        self.wfile.write(f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nConnection:close\r\n\r\n".encode("utf-8")) 
        cpick = self.comp_pick()
        self.draw_grid(x,y,cpick)
         

ss = server.HTTPServer(("0.0.0.0",8005),SubmarineHandler)
ss.serve_forever()