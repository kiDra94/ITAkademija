from http.server import HTTPServer, BaseHTTPRequestHandler
#importujemo HTTPServer i BaseHTTPRequestHandler klase iz modula http.server 

#importujemo modul urllib.parse odn. metodu parse_qs koja sluzi za raščlanjivanje upitnih stringova u Pythonu
from urllib.parse import parse_qs

#definisemo recnik podataka
names_dict = {'Pera':'Peric',
            'Mika':'Mikic',
            'Mihajlo':'Mihajlovic',
            'Marko':'Markovic'}


#pravimo klasu RequestHandler koja nasledjuje klasu BaseHTTPRequestHandler
class RequestHandler(BaseHTTPRequestHandler):    
    #definisemo GET metodu
    def do_GET(self):
    	
        #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
        self.log_message("Incoming GET request...")  
        #Pokusavamo da izdvojimo podatak name koji client salje
        try:
            '''razvajamo upitni string pomoću funkcije parse_qs.
            Pomocu path polja nasleđene BaseHTTPRequestHandler klase dobijamo string objekat. Pošto nam ono vraća ceo upitni string (/?name=michael),
            a mi ne želimo da nam u ključ rečnika uđu karakteri / i ?, koristićemo odsečak tog stringa: parse_qs(self.path[2:]). Izdvajamo ime kao prvi element liste'''
            name = parse_qs(self.path[2:])['name'][0]
        except:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Incorrect parameters provided')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Incorrect parameters provided")
            return

        #ako se ime nalazi medju kljucevima u recniku vracamo statusni kod 200 i prezime za dato ime preko metode send_response_to_client
        if name in names_dict.keys():
            self.send_response_to_client(200, names_dict[name])
        else:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Name not found')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Name not found")
 
 
 
 
    def do_POST(self):
        #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
        self.log_message('Incoming POST request...')
        
        '''razvajamo upitni string pomoću funkcije parse_qs.
            Pomocu path polja nasleđene BaseHTTPRequestHandler klase dobijamo string objekat. Pošto nam ono vraća ceo upitni string (/?name=peter&last_name=peterson.),
            a mi ne želimo da nam u ključ rečnika uđu karakteri / i ?, koristićemo odsečak tog stringa: parse_qs(self.path[2:]).'''
        data = parse_qs(self.path[2:])
        try:
            #Pokusavamo da dodamo novi par u recnik
            names_dict[data['name'][0]] = data['last_name'][0]
            # vracamo statusni kod 200 i ceo recnik preko metode end_response_to_client
            self.send_response_to_client(200, names_dict)
        except KeyError:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Incorrect parameters provided')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Incorrect parameters provided")
 
 
 
    #definisemo metodu za slanje odgovora klientu koja ce biti zaduzena za slanje statusnog koda, zaglavlja i tela poruke
    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        #vraca se recnik sa statusnim kodovima i porukama
        
        #salje se zaglavlje pomocu send_header(), koja za parametre prima dva elementa: ime polja zaglavlja i njegovu vrednost-jedno polje zaglavlja po jednom pozivu ove metode
        self.send_header('Content-type', 'text/plain')
       
        #naglasavamo gde je kraj čitavog zaglavlja
        self.end_headers()
 
        #pakujemo podatke
        self.wfile.write(str(data).encode())
 

server_address = ('127.0.0.1', 8080)
#definisemo adresu i port

#iniciamo serverski objekat
http_server = HTTPServer(server_address, RequestHandler)

#Pokrenućemo serverski objekat pomoću HTTPServer metode serve_forever().
http_server.serve_forever()
