from http.server import HTTPServer, BaseHTTPRequestHandler


from urllib.parse import parse_qs

drzave_dict = {'Srbija':['Beograd', 88361, 7498001],
              'Hrvatska':['Zagreb',56594, 3888529]}
            
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self): 

        self.log_message("Incoming GET request...")  
        try:
            grad =parse_qs(self.path[2:])['drzava'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return
 
        if grad in drzave_dict.keys():
            self.send_response_to_client(200, drzave_dict[grad])
        else:
            self.send_response_to_client(404, 'Country not found')
            self.log_message("Country not found")
 
 
 
 
    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            drzave_dict[data['drzava'][0]] = [data['grad'][0],data['povrsina'][0],data['broj_stanovnika'][0]]
            self.send_response_to_client(200, drzave_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
 
 
    def do_DELETE(self):
        self.log_message('Incoming DELETE request...')
        
        try:
            drzava = parse_qs(self.path[2:])['drzava'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return
        
        if drzava in drzave_dict.keys():
            drzave_dict.pop(drzava)
            self.send_response_to_client(200, drzave_dict)
            
        else:
            self.send_response_to_client(404, 'Country does not exist')
            self.log_message("Country does not exist")    
           
       
 

 
    def send_response_to_client(self, status_code, data):
        
        self.send_response(status_code)   
        self.send_header('Content-type', 'text/plain')

        self.end_headers()

        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)


http_server = HTTPServer(server_address, RequestHandler)

http_server.serve_forever()
