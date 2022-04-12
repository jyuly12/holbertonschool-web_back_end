var http = require('http');

//create a server object:
http.createServer(function (req, app) {
  app.write('Hello Holberton School!'); //write a response to the client
  app.end(); //end the response
}).listen(1245); //the server object listens on port 1245