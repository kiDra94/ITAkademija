from http.server import HTTPServer, BaseHTTPRequestHandler
#importujemo HTTPServer i BaseHTTPRequestHandler klase iz modula http.server 

#importujemo modul urllib.parse odn. metodu parse_qs koja sluzi za raščlanjivanje upitnih stringova u Pythonu
from urllib.parse import parse_qs

#definisemo recnik podataka
slova_dict = {'a':'A',
              'b':'B',
              'c':'C',
              'd':'D'}
            


class RequestHandler(BaseHTTPRequestHandler):
    
    
    #definisemo GET metodu
    def do_GET(self): 

        #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
        self.log_message("Incoming GET request...")  
        
        #Pokusavamo da izdvojimo podatak malo_slovo koji client salje
        try:
            '''razvajamo upitni string pomoću funkcije parse_qs.
            Pomocu path polja nasleđene BaseHTTPRequestHandler klase dobijamo string objekat. Pošto nam ono vraća ceo upitni string (/?malo_slovo=a),
            a mi ne želimo da nam u ključ rečnika uđu karakteri / i ?, koristićemo odsečak tog stringa: parse_qs(self.path[2:]). Izdvajamo malo_slovo kao prvi element liste'''
            slovo =parse_qs(self.path[2:])['malo_slovo'][0]
        except:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Incorrect parameters provided')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Incorrect parameters provided")
            return
 
        if slovo in slova_dict.keys():
            #ako se malo slovo nalazi medju kljucevima u recniku vracamo statusni kod 200 i veliko slovo za dato malo slovo preko metode send_response_to_client
            self.send_response_to_client(200, slova_dict[slovo])
        else:
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Letter not found')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Letter not found")
 
 
 
 
    def do_POST(self):
        #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
        self.log_message('Incoming POST request...')
        
        '''razvajamo upitni string pomoću funkcije parse_qs.
            Pomocu path polja nasleđene BaseHTTPRequestHandler klase dobijamo string objekat. Pošto nam ono vraća ceo upitni string (/?name=peter&last_name=peterson.),
            a mi ne želimo da nam u ključ rečnika uđu karakteri / i ?, koristićemo odsečak tog stringa: parse_qs(self.path[2:]).'''
        data = parse_qs(self.path[2:])
        try:
            #Pokusavamo da dodamo novi par u recnik
            slova_dict[data['malo_slovo'][0]] = data['veliko_slovo'][0]
             # vracamo statusni kod 200 i ceo recnik preko metode end_response_to_client
            self.send_response_to_client(200, slova_dict)
        except KeyError:  
            #Vracamo statusni kod 404 i ime greske preko metode end_response_to_client
            self.send_response_to_client(404, 'Incorrect parameters provided')
            #Ispis poruke pomocu metode log_message klase BaseHTTPRequestHandler
            self.log_message("Incorrect parameters provided")
 
 
 
    #definisemo metodu za slanje odgovora klientu koja ce biti zaduzena za slanje statusnog koda, zaglavlja i tela poruke
    def send_response_to_client(self, status_code, data):
        #vraca se recnik sa statusnim kodovima i porukama
        self.send_response(status_code)   
        #salje se zaglavlje pomocu send_header(), koja za parametre prima dva elementa: ime polja zaglavlja i njegovu vrednost-jedno polje zaglavlja po jednom pozivu ove metode
        self.send_header('Content-type', 'text/plain')

        '''Takodje, nakon sto odredimo koja polja zaglavlja saljemo, koristimo metodu end_headers() kako bismo naznacili gde je kraj citavog zaglavlja, a odakle, opciono, pocinje deo sa podacima koji se salju. '''
        self.end_headers()

        '''wfile predstavlja konekciju izmedju klijenta i servera u koju se moze samo upisivati. Bilo koji podaci upisani u tu konekciju metodom write() se odmah salju kao odgovor na klijentski zahtev. Parametar metode write() je tipa bytes i zato, ako saljemo stringove, moramo koristiti string metodu encode(), koja ce str objekat pretvoriti u bytes.'''
        self.wfile.write(str(data).encode())
 
 
server_address = ('127.0.0.1', 8080)
#definisemo adresu i port

#iniciamo serverski objekat
http_server = HTTPServer(server_address, RequestHandler)

#Pokrenućemo serverski objekat pomoću HTTPServer metode serve_forever().
http_server.serve_forever()