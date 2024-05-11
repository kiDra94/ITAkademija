from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
student_dict = {'12':['Vukasin', 'Baresic', 'Beograd'],'145':['Pera', 'Peric', 'Novi Sad'],'134':['Lazar', 'Lazic', 'Zrenjanin'],'14':['Ana', 'Stanic', 'Sremska Mitrovica']}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            index = parse_qs(self.path[2:])['index'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return

        if index in student_dict.keys():
            self.send_response_to_client(200, student_dict[index])
        else:
            self.send_response_to_client(400, 'Index not found')
            self.log_message("Index not found")

    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            student_dict[data['index'][0]] = [data['name'][0], data['last_name'][0], data['city'][0]]
            self.send_response_to_client(200, student_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
             
    def send_response_to_client(self, status_code, data):
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
     
        # Send the response
        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()

