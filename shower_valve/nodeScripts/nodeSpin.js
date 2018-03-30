var Gpio = require('onoff').Gpio;
var sleep = require('sleep');
//const reaLine = require('readline');

var dirPin0 = new Gpio(13, 'out');
var dirPin1 = new Gpio(19, 'out');
var stepPin = new Gpio(26, 'out');

//ask how long to spin
var len = 500;
var loops = 2;
var mDelay = 300; //milisecond delay

var func = clockWise;

var dir0 = 0;
var dir1 = 1;

var start = setInterval(spin, len);


function spin() {

  process.stdout.write("inside the loop");
 
  dirPin0.writeSync(dir0);   //flip-flop these to change direction
  dirPin1.writeSync(dir1);

  process.stdout.write("set the dirPins");
  
  for (var i = 0; i < loops; i++) {
    process.stdout.write(" step " + i);
   stepPin.writeSync(1);
   sleep.msleep(mDelay);
   stepPin.writeSync(0);
  }
}


// function clockWise() {

//   process.stdout.write("inside the loop");
 
//   dirPin0.writeSync(1);   //flip-flop these to change direction
//   dirPin1.writeSync(0);

//   process.stdout.write("set the dirPins");
  
//   for (var i = 0; i < loops; i++) {
//     process.stdout.write(" step " + i);
//    stepPin.writeSync(1);
//    sleep.msleep(mDelay);
//    stepPin.writeSync(0);
//   }
// }

// function counterClockWise() {

//   process.stdout.write("inside the loop");
 
//   dirPin0.writeSync(0);   //flip-flop these to change direction
//   dirPin1.writeSync(1);

//   process.stdout.write("set the dirPins");
  
//   for (var i = 0; i < loops; i++) {
//     process.stdout.write(" step " + i);
//    stepPin.writeSync(1);
//    sleep.msleep(mDelay);
//    stepPin.writeSync(0);
//   }
// }

//break ON and OFF into their own seperate functions and use "setTimeout(func1, mDelay);""

function endLoop() { //function to stop blinking
  clearInterval(start); // Stop blink intervals
  dirPin0.writeSync(0);
  dirPin1.writeSync(0);
  stepPin.writeSync(0);
  dirPin0.unexport();
  dirPin1.unexport();
  stepPin.unexport();
}

setTimeout(endLoop, len); //stop blinking after 5 seconds
 
process.on('SIGINT', function () {
  dirPin0.writeSync(0);
  dirPin1.writeSync(0);
  stepPin.writeSync(0);
  dirPin0.unexport();
  dirPin1.unexport();
  stepPin.unexport();
});
