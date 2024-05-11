from http.server import HTTPServer, BaseHTTPRequestHandler
localisation_dict = {'en':'Greetings!', 'es':'Saludos!'}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message
        ("Incoming GET request with headers {}".format(self.headers.items()))
        try:
            self.send_response_to_client(200, localisation_dict[self.headers.get('Accept-Language')])
        except:
            self.send_response_to_client(404, 'Incorrect language code provided')
            self.log_message("Incorrect language code provided")
            return
    def send_response_to_client(self, status_code, data):
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Send the response
        self.wfile.write(str(data).encode())
server_address = ('127.0.0.1', 8000)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()