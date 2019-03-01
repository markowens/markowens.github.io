var http = require('http');
var dt = require('./myFirstModule');
var url = require('url');
var fs = require('fs');
var uc = require('upper-case')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('The date and time is currently: ' + dt.myDateTime());
    res.write("<hr/>");
    res.write(uc('This request came from: ') + req.url);
    res.write('<hr/>');
    var q = url.parse(req.url, true).query;
    var txt = q.year + " " + q.month;
    res.write(txt);
    res.end();
}).listen(8080);