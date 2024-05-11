import eventlet
 
import socketio
 
sio_server = socketio.Server()
 
app = socketio.WSGIApp(sio_server)
 
@sio_server.event
 
def connect(sid, headers):
 
    print('Client connected: ', sid)
 
@sio_server.event
 
def my_message(sid, data):
 
    print('User "{}", send message:{}'.format(data['name'], data['msg']))
 
eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)