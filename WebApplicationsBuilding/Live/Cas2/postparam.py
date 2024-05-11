import http.server as server 

class Handler(server.SimpleHTTPRequestHandler):

    def draw_form(self):
        self.wfile.write(b"<form method='post'><input type='text' name='username' /><input type='submit' value='Say Hello' /></form>")

    def do_POST(self): 
        print("Pozvala se metoda POST")
        len = int(self.headers["Content-Length"])
        data = self.rfile.read(len).decode("utf-8")
        params = data.split('=')
        print(params)
        #name = params["name"]
        name = params[1]
        print(name)
        self.wfile.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close\r\n\r\n") 
        self.wfile.write(f"Hello {name}<hr>".encode("utf-8"))
        self.draw_form()

    def do_GET(self):  
        print("Pozvala se metoda GET")
        self.wfile.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close\r\n\r\n") 
        self.draw_form() 

ss = server.HTTPServer(("0.0.0.0",8005),Handler)
ss.serve_forever()