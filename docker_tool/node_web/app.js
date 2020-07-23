//import 하는 부분 
const http=require("http");
//
const os=require("os");
// 콘솔 로그 찍고 웹서버 시작됬다 
console.log("weberver starting...");
// 
var handler=function(request, response){
    console.log("Received request from "+request.connection.remoteAddress);
    response.writeHead(200);
    response.end("<h1>You've hit  "+os.hostname()+"</h1>\n");
};

var www = http.createServer(handler);

www.listen(80);

