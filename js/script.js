
let game;

//------------------
function setup() {
  game = new Game();
  game.setup();
}

//------------------
function draw() {
  background(0);
  game.update();
  game.draw();
}


//------------------
function keyPressed() {
  game.inputKey(keyCode);
}
