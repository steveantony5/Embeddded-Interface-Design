import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
      
    def on_message(self, message):
        print 'message received:  %s' % message
        
        if message == "sensor":
            self.write_message("buttons 23.33 23.33")
            
        
        elif message == "last db readings":
            self.write_message("buttons")
            self.write_message("233.33")
            self.write_message("233.33")
            
        elif message == "temp history":
            self.write_message("history add")
            
        elif message == "humidity history":
            self.write_message("history add 2")
            
        elif message == "temp graph":
            self.write_message("temp graph add")
            
        elif message == "Hum graph":
            self.write_message("Hum graph add")
            
            
 
    def on_close(self):
        print 'connection closed'
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()
