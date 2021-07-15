var http = require('http'); // 전처리기
http.createServer(function (request, response){
    response.writeHead(200, {'Content-Type' : 'text/plain'}); // 200 : OK
    response.end('Hello Node.Js\n');
}).listen(8080, '127.0.0.1')

console.log('Server is Running at http://127.0.0.1:8080/');