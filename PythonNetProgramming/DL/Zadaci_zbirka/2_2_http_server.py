from http.server import HTTPServer, BaseHTTPRequestHandler


from urllib.parse import parse_qs

slova_dict = {'a':'A',
              'b':'B',
              'c':'C',
              'd':'D'}
            


class RequestHandler(BaseHTTPRequestHandler):
    
    

    def do_GET(self): 

        self.log_message("Incoming GET request...")  
        try:
            slovo =parse_qs(self.path[2:])['malo_slovo'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return
 
        if slovo in slova_dict.keys():
            self.send_response_to_client(200, slova_dict[slovo])
        else:
            self.send_response_to_client(404, 'Letter not found')
            self.log_message("Letter not found")
 
 
 
 
    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            slova_dict[data['malo_slovo'][0]] = data['veliko_slovo'][0]
            self.send_response_to_client(200, slova_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
 
 
 
 
    def send_response_to_client(self, status_code, data):
        
        self.send_response(status_code)   
        self.send_header('Content-type', 'text/plain')

        '''Takodje, nakon sto odredimo koja polja zaglavlja saljemo, koristimo metodu end_headers() kako bismo naznacili gde je kraj citavog zaglavlja, a odakle, opciono, pocinje deo sa podacima koji se salju. '''
        self.end_headers()

        '''wfile predstavlja konekciju izmedju klijenta i servera u koju se moze samo upisivati. Bilo koji podaci upisani u tu konekciju metodom write() se odmah salju kao odgovor na klijentski zahtev. Parametar metode write() je tipa bytes i zato, ako saljemo stringove, moramo koristiti string metodu encode(), koja ce str objekat pretvoriti u bytes.'''
        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)


http_server = HTTPServer(server_address, RequestHandler)

http_server.serve_forever()
