var express=require("express");
var app = require('express');
var exphbs = require('express-handlebars');
var path = require('path');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
const async=require('async');
const assert = require('assert');
const Storage = require('dom-storage');
 
var dataStorage = new Storage('./db.json', { strict: false, ws: '  ' });


// Init App
var app = express();
app.set('port', (process.env.PORT || 3000));

var server = app.listen(app.get('port'), function(){
  console.log('Server started on port '+app.get('port'));
});

// BodyParser Middleware
// used for handlebars data rendering with server
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

class Bus {
    constructor(data){
        this.busName = data['busName'],
        this.source = data['source'],
        this.destination = data['destination'],
        this.startDay = data['startDay'],
        this.startMonth = data['startMonth'],
        this.startYear = data['startYear'],
        this.endDay = data['endDay'],
        this.endMonth = data['endMonth'],
        this.endYear = data['endYear'],
        this.busDays = new Set(data['freq']),
        this.capacity = data['capacity']
    }
}

app.post('/registerBus', function(req, res, next){
    // Bus number will be unique
    // key
    busNumber = req.body.busNumber;
    // new bus registered
    let bus = new Bus(req.body);
    dataStorage.setItem(busNumber, bus);
})

app.post('/searchBus', function(req, res, next){
    let source = req.body.source;
    let destination = req.body.destination;
    let day = req.body.day
    let month = req.body.month
    let year = req.body.year

    





})
