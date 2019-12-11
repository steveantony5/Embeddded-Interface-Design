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
 * @\date	10/07/2019
 *
 */

const http = require('http');
const sqlite3 = require('sqlite3').verbose();
const WebSocketServer = require('websocket').server;
database = r"c:\sqlite\db\eidproject.db"
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
let db = new sqlite3.Database(database);

//Contiously listen on the connected port
wsServer.on('request', function(request) {
    
	//Accept the client connections
    const connection = request.accept(null, request.origin);
    
    connection.on('message', function(message) {
        
        console.log('Received Message:', message.utf8Data);
        
		//Check for the requested data
        if (message.utf8Data == "get_data") {
		
		db.all("select * from magicwand", function(err, allRows) {

			if (err != NULL) {
				console.log(err);
			}
				
			console.log(util.inspect(allRows))
			//Jsonize the obtained data
			ret = JSON.stringify(allRows);
			console.log(ret);
					
			//Send querry results to the client
			connection.sendUTF(ret);
		});
        }

        
        if (message.utf8Data == "get_sensor") {
            
			//Querry the MYSQL database to obtain lastest teamperature and humidity data from MYSQL
            con.query("select * from magicwand order by id desc limit 1", function (err, result, fields) {
				
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
