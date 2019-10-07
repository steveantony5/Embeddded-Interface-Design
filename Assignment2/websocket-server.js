/***************************************************************************************************
MIT License

Copyright (c) 2019 Sorabh Gandhi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
****************************************************************************************************/

/**
 * @\file	websocket-server.js
 * @\author	Sorabh Gandhi
 * @\brief	This file contains server side implementation of handling client request and 
 *			quering the mysql data and sending back to the client
 * @\date	10/06/2018
 *
 */

const http = require('http');
var mysql = require('mysql');
const WebSocketServer = require('websocket').server;

var ret = [];

//Create an http server object
const server = http.createServer();

//listen to an specified port
server.listen(9898);

//Create an object for web socket server
const wsServer = new WebSocketServer({
    httpServer: server
});

//Create connection to the MYSQL database
var con = mysql.createConnection({
    
    host: "localhost",
    user: "gandhi",			//Specify the username
    password: "sorabh",		//password
    database: "sensordb"	//database name
});

//Connect to the database and get a connection handle
con.connect(function(err) {
    //Check if its a valid connection
    if (err) {
        console.error('Error connecting: ' + err.stack);
        return;
    }
    
    console.log('Connected as id ' + con.threadId);
});

//Contiously listen on the connected port
wsServer.on('request', function(request) {
    
	//Accept the client connections
    const connection = request.accept(null, request.origin);
    
    connection.on('message', function(message) {
        
        console.log('Received Message:', message.utf8Data);
        
		//Check for the requested data
        if (message.utf8Data == "get_humidity") {
			
			con.query("SHOW TABLES LIKE 'sensordata'", function (err, result, fields) {
			
			if (result) {
				//Querry the MYSQL database to obtain last 10 humidity value
				con.query("select humidity from sensordata order by id desc limit 10", function (err, result, fields) {
					
					//Jsonize the obtained data
					ret = JSON.stringify(result);
					console.log(ret);
					
					//Send querry results to the client
					connection.sendUTF(ret);
				});
			} else {
                connection.sendUTF('error');
            }

			});
        }

        
        if (message.utf8Data == "get_sensor") {
            
			//Querry the MYSQL database to obtain lastest teamperature and humidity data from MYSQL
            con.query("select temperature, humidity from sensordata order by id desc limit 1", function (err, result, fields) {
				
				//Jsonize the obtained data
                ret = JSON.stringify(result);
                console.log(ret);
				
				//Send querry results to the client
                connection.sendUTF(ret);
            });
        }
    });
    
	//Disconnect if the client is closed
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });
});
