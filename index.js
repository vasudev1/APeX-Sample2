// var keepLooping = false;
var mqtt = require('mqtt')
var client = mqtt.connect('mqtt://host')



//var values = {

//	'accelerometer': [],
//	'temperature': 0
//};

var values = {

     'accelX': 0,
     'accelY': 0,
     'accelZ': 0,
     'temperature': 0
};


while (true) {

     //Accelerometer Data
     x = random(0, 1);
     y = random(0, 1);
     z = random(0, 1);

     // Temperature Data in Fahrenheit
     // @TODO:Linear interpolator instead of random. 	
     temp = random(0, 110);
     
     //values.accelerometer.push({'x': x});
     //values.accelerometer.push({'y': y});
     //values.accelerometer.push({'z': z});
     values.accelX = x;
     values.accelY = y;
     values.accelZ = z;
     values.temperature = temp;
     console.log('Values: ' + JSON.stringify(values));
     client.publish('apex_mqtt', JSON.stringify(values));

     // 
     
}; // while loop


function random (low, high) {
	return Math.random() * (high - low) + low;
}

process.on( 'SIGINT', function() {
  console.log( "\nGracefully shutting down from SIGINT (Ctrl-C)" );
  // some other closing procedures go here
  client.end()
  process.exit( );
})