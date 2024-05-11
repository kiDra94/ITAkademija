import socketio  
 
ime = input("Tvoje ime je:") 
prezime=input("Tvoje prezime je:")
sio_client = socketio.Client()

def send_msg():
 
    while True:
 
        poruka = input("Poruka: ")
 
        sio_client.emit('my_message', {'msg': poruka, 'name':ime,'surname':prezime})
 
        sio_client.sleep(1) 
 
 
@sio_client.event
def connect():
    print('connection established')
 
    send_msg() 

 
sio_client.connect('http://localhost:5000')
 
sio_client.wait() 
