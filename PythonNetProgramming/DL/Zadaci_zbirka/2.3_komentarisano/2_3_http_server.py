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
 
    #definisemo DELETE metodu
    def do_DELETE(self):
        #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler        
        self.log_message('Incoming DELETE request...')
        
        #Pokusavamo da izdvojimo podatak name koji client salje  
        try:
            '''razvajamo upitni string pomoću funkcije parse_qs.
            Pomocu path polja nasleđene BaseHTTPRequestHandler klase dobijamo string objekat. Pošto nam ono vraća ceo upitni string (/?malo_slovo=a),
            a mi ne želimo da nam u ključ rečnika uđu karakteri / i ?, koristićemo odsečak tog stringa: parse_qs(self.path[2:]). Izdvajamo malo_slovo kao prvi element liste'''
            malo_slovo = parse_qs(self.path[2:])['malo_slovo'][0]
        except:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Incorrect parameters provided')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Incorrect parameters provided")
            return
        
        if malo_slovo in slova_dict.keys():
            #ako se malo slovo nalazi medju kljucevima u recniku:
            # brisemo par iz recnika za dati kljuc koji se nalazi u promenljivi malo_slovo
            # vracamo statusni kod 200 i ceo recnik preko metode send_response_to_client
            slova_dict.pop(malo_slovo)
            self.send_response_to_client(200, slova_dict)
            
        else:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Name does not exist')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Name does not exist")    
           
       
 

 
    def send_response_to_client(self, status_code, data):
        
        self.send_response(status_code)   
        self.send_header('Content-type', 'text/plain')

        self.end_headers()

        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)


http_server = HTTPServer(server_address, RequestHandler)

http_server.serve_forever()
