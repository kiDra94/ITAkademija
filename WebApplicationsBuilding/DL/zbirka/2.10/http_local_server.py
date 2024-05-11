from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
student_dict = {'12':['Vukasin', 'Baresic', 'Beograd'],'145':['Pera', 'Peric', 'Novi Sad'],'134':['Lazar', 'Lazic', 'Zrenjanin'],'14':['Ana', 'Stanic', 'Sremska Mitrovica']}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            city = parse_qs(self.path[2:])['city'][0]
            
            if city.isalpha()==False:
                self.send_response_to_client(404, 'Not all characters are letters')
                self.log_message("Not all characters are letters")
                return
            
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return

        lista=[]
        for el in student_dict:
            if(student_dict[el][2]==city):
                lista.append(student_dict[el])
        self.send_response_to_client(200,lista)


    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            student_dict[data['index'][0]] = [data['name'][0], data['last_name'][0], data['city'][0]]
            self.send_response_to_client(200, student_dict)
        except:
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