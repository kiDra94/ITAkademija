import socketio
 
username = input("Your username is:")
 
sio_client = socketio.Client()
 
def send_msg():
 
    while True:
 
        msg = input("Enter message: ")
 
        sio_client.emit('my_message', {'msg': msg, 'name':username})
 
sio_client.sleep(1) # wait for 1 sec and ask user again for message
 
 
@sio_client.event
 
def connect():
 
    print('connection established')
 
    send_msg()   
 
sio_client.connect('http://localhost:5000')
 
sio_client.wait() # Wait until server ends the connection