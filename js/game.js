class Game {
    constructor() {
      this.rotIndex = 0;  
      this.lines = []; 
      this.score = 0;
      this.points_per_level=100
      this.level=1
      this.game_over = false;
      this.chrono=millis();
      this.timeLevel=1000;
      this.shape= null;
      this.nextShape = null;
    }
  
    setup() {
      createCanvas(200+100, 400);
      rectMode(CENTER);
      this.shape = new Shape(10,10);
      this.nextShape = new Shape(width-70, 50);
    }
  
    update(){
       if (this.game_over) return;
        this.makeStepDown();
        if (!this.shape.canMoveDown(this.lines) || this.nextOnFloor()) { 
          this.shape.move(0, -20);
          this.lockCurrentShape();  
          this.switchToNextShape();
          this.checkUpdateScore();
        }
      }
  
    draw(){
      this.displayGrid();
      this.shape.draw();
      this.drawLines();
      this.displaySideBoard();
      if (this.game_over) {
          fill(255,100,100);
          text("Game Over", width-80, height/2+150);
      }
    }
    
    makeStepDown(){ 
      if (millis() - this.chrono > this.timeLevel) {
        this.chrono = millis();
        this.shape.move(0, 20);
      }
    }
  
    nextOnFloor(){
      return !(this.shape.highestY() < height)
    }
    
    switchToNextShape(){
      this.rotIndex = 0;
      this.chrono = millis();
      this.shape = this.nextShape;
      this.shape.setXoffset(10);
      this.shape.setYoffset(10);
      this.nextShape = new Shape(width-70, 50);
    }
  
    displaySideBoard() {
      fill('#222222');
      rect(width-50, height/2, 100, height);
      this.nextShape.draw()
      fill(130)
      textSize(15)
      text("Level "+this.level, width-80, height/2)
      text("Score "+this.score, width-80, height/2+50)
    }
  
    displayGrid() {
      noFill();
      stroke(180)
      strokeWeight(0.1)
      for (let y = 10; y < height; y += 20) {
        for (let x = 10; x < width-100; x += 20) {
          rect(x, y, 20, 20);
        }
      }
    }
  
    lockCurrentShape() {  
      let arr = this.shape.getRealCoords();
      for (let i = 0; i < arr.length; i++) {
        this.lines.push(arr[i]);
      }
    }
  
    checkUpdateScore(){
      for (let i = 0; i < this.lines.length; i++) {
        let row = height - i * 20 - 10;
        const count = this.lines.filter(item => item.y === row).length;
        if (count == 10) {
          this.removeLine(row);
          this.score+=20;
          if (this.score > this.points_per_level*this.level) {
            this.score=0;
            this.level++;
          }
        }
      }
      const over = this.lines.filter(item => item.y < 30).length;
      this.game_over= over != 0;
    }
  
    removeLine(row){
      this.lines = this.lines.filter((item) => item.y != row);
      for (let i = 0; i < this.lines.length; i++) {
        let ln = this.lines[i];
        if (ln.y < row) ln.y += 20;
        this.lines[i].y = ln.y;
      }
    }
  
    drawLines() {
      for (let i = 0; i < this.lines.length; i++) {
        let ln = this.lines[i];
        fill(ln.col);
        rect(ln.x, ln.y, 20, 20)
      }
    }
  
    inputKey(key){
  
      let x, y;
  
      if (key == RIGHT_ARROW) {
        x = this.shape.getXoffset();
        if (x < width-100 - 20 * this.shape.getNbX()) this.shape.move(20,0);
      }
    
      if (key == LEFT_ARROW) {
        x= this.shape.getXoffset();
        if (x > 20) this.shape.move(-20,0);
      }
      
      if (key == DOWN_ARROW) {
        y=this.shape.getYoffset();
        if (y < height-20) this.shape.move(0,20);
      }
    
      if (key == UP_ARROW) {
        let save =this.rotIndex;
        this.rotIndex++;
        this.rotIndex = this.rotIndex % 4;
        // disable rotation to prevent overflow
        this.shape.rotate(this.rotIndex);
        if (this.shape.xOutRightSide(width-100)) {
          this.rotIndex = save;
        }
        this.shape.rotate(this.rotIndex);
      }   
    }
  
    
  } // class
  