var mysql = require('mysql');

var con = mysql.createConnection( {
    host: "localhost",
    user: "root",
    password: "mydb"
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    con.query("CREATE DATABASE db1", function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
  }); 