const http = require('http');
const WebSocketServer = require('websocket').server;

const server = http.createServer();
server.listen(9898);

const wsServer = new WebSocketServer({
    httpServer: server
});

var mysql = require('mysql');
var ret = [];

var con = mysql.createConnection({
    
    host: "localhost",
    user: "gandhi",
    password: "sorabh",
    database: "sensordb"
});

con.connect(function(err) {
    
    if (err) {
        console.error('Error connecting: ' + err.stack);
        return;
    }
    
    console.log('Connected as id ' + con.threadId);
});

wsServer.on('request', function(request) {
    
    const connection = request.accept(null, request.origin);
    
    connection.on('message', function(message) {
        
        console.log('Received Message:', message.utf8Data);
        
        if (message.utf8Data == "get_humidity") {
            
            con.query("select humidity from sensordata order by id desc limit 10", function (err, result, fields) {
                ret = JSON.stringify(result);
                console.log(ret);
                connection.sendUTF(ret);
            });
        }

        
        if (message.utf8Data == "get_sensor") {
            
            con.query("select temperature, humidity from sensordata order by id desc limit 1", function (err, result, fields) {
                ret = JSON.stringify(result);
                console.log(ret);
                connection.sendUTF(ret);
            });
        }
    });
    
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });
});
