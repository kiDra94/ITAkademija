import http.server as server 
import importlib
 
class DynamicRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        page = self.path.replace("/","")
        page = f"{page}_mod"
        print(page)
        try:
            module = importlib.import_module(page)
            self.send_response(200) 
            self.send_header("Content-Type","text/html")
            self.send_header("Connection","Close")
            self.end_headers()
            module.do_GET(self)
        except:
            return super().do_GET()
 
ss = server.HTTPServer(("0.0.0.0",8005),DynamicRequestHandler)
ss.serve_forever()