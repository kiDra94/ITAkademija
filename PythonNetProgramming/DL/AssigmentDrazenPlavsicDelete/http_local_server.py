from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
names_dict = {'john':'smith',
            'david':'jones',
            'michael':'johnson',
            'chris':'lee'}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            name = parse_qs(self.path[2:])['name'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return
 
        if name in names_dict.keys():
            self.send_response_to_client(200, names_dict[name])
        else:
            self.send_response_to_client(404, 'Name not found')
            self.log_message("Name not found")
 
    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            names_dict[data['name'][0]] = data['last_name'][0]
            self.send_response_to_client(200, names_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")

    def do_DELETE(self):
        self.log_message('Incoming DELETE request...')
        try:
            name = parse_qs(self.path[2:])['name'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return

        if name in names_dict:
            del names_dict[name]
            self.send_response_to_client(200, f"Name '{name}' deleted. Updated dictionary: {names_dict}")
        else:
            self.send_response_to_client(404, f"Name '{name}' not found")
            self.log_message(f"Name '{name}' not found")
 
    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()