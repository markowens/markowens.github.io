var nodemailer = require('nodemailer');
var readline = require('readline');


var rl = readline.createInterface(process.stdin, process.stdout);

rl.question("Enter password: " , (pwd) => {

    var transporter = nodemailer.createTransport( {
        server: 'gmail',
        auth: {
            user: 'jmolist@gmail.com',
            pass: pwd
        }
    });

    var mailOptions = {
        from: 'jmolist@gmail.com',
        to: 'jmarkphoto@gmail.com',
        subject: 'test node',
        text: "This is a node email"
    };

    transporter.sendMail(mailOptions, function(error, info) {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });

    rl.close();
});







