var express = require('express');
var router = express.Router();
var http = require('http');
var server = http.createServer(express);
var io = require('socket.io').listen(server);
/* GET home page. */
router.get('/', function(req, res) {
  //res.render('index', { title: 'Express' });
    res.sendfile('index.html')
});

io.sockets.on('connection', function (socket) {
    socket.emit('news', { hello: 'world' });
    socket.on('my other event', function (data) {
        console.log(data);
    });
});

module.exports = router;
