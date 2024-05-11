#importujemo biblioteku koja pruža olaškano, konkurentno upravljanje mrežom.
import eventlet
# importujemo biblioteku koja nam omogućava rad sa WebSocketima
import socketio
 
#kreiramo serverski objekat koji ćemo nazvati sio_server
sio_server = socketio.Server() 

#Postavljamo nas kod servera na server
app = socketio.WSGIApp(sio_server)

#Funkciju connect dekorišemo sio_server.event funkcijom kako bi predstavlala dogadjaj
@sio_server.event
def connect(sid, headers):
    print('Client connected: ', sid)
 
 
#Funkciju my_messge dekorišemo sio_server.event funkcijom kako bi predstavlala dogadjaj
@sio_server.event
def my_message(sid, data):
    print('Ime "{}", Prezime "{}" poruka:{}'.format(data['name'],data['surname'], data['msg']))
 
#stavljamo server u stanje osluškivanja naredbom:
eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)

