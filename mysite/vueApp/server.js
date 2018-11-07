var express = require('express');
var path = require('path');
var serveStatic = require('serve-static');
app = express();
app.use(serveStatic(__dirname + "/dist"));

app.get('/', function(req, res){
  // res.send('hello');
  res.render(index.html);
});

var port = Number(process.env.PORT || 8080);
app.listen(port);
console.log('server started '+ port);