let tetrominoes=[I_, O_, T_, J_, L_, S_, Z_];  
let colrs=['#ff0000','#00ff00','#0000ff','#ffff00',  
                                '#ff00ff','#00ffff', '#ffffff']; // ex cols


class Shape {
  constructor(x, y) {
    this.x = x || 10;
    this.y = y || 10;
    this.rotIndex=0;
    this.pattern=random(tetrominoes);
    this.p = this.pattern[this.rotIndex];
    this.c =colrs[tetrominoes.indexOf(this.pattern)];
  }

  getXoffset(){
    return this.x;
  }

  getYoffset(){
    return this.y;
  }
  
  setXoffset(x){
    this.x=x;
  }

  setYoffset(y){
    this.y=y;
  }

  rotate(rot){
    this.rotIndex=rot;
    this.p = this.pattern[this.rotIndex];
  }
  
  getPattern(){
    return this.p;
  }

  getColor(){
    return this.c;
  }

  move(x, y) {
    this.x += x;
    this.y += y;
  }
  
  draw(){
    fill(this.c);
    for (let i = 0; i < this.p.length; i++) {
      let s = this.p[i];
      let x = s.x * 20 + this.x;
      let y = s.y * 20 + this.y;
      rect(x, y, 20, 20);
    }
  }

  maxY() {
    return (Math.max.apply(Math, this.p.map(function(o){return o.y})));
    // let largest = 0;
    // this.p.forEach(function(elem) {
    //   if (largest < elem.y)
    //     largest = elem.y;
    // });
    // return largest;
  }

  getNbX() {
  let largest = 0;
  this.p.forEach(function(elem) {
    if (largest < elem.x)
      largest = elem.x;
  });
  return largest + 1;
}

 xOutRightSide(limit){
    for (let i = 0; i < this.p.length; i++) {
      let s = this.p[i];
      let x= s.x*20+this.x;
      if (x>limit) return true;
    }
    return false;
  }

  canMoveDown(wall){
    for (let i = 0; i < wall.length; i++) {
      let ln = wall[i];
      for (let j = 0; j < 4; j++) {
        let a = this.p[j].x * 20 + this.x;
        let b = this.p[j].y * 20 + this.y;
        if ((a == ln.x) &&
          (b == ln.y)) return false;
      }
    }
    return true;
  }

  highestY(){
    return (this.y + 20 * this.maxY())
  }

  getRealCoords(){
    let ret=[];
    let _x, _y;

    for (let i = 0; i < this.p.length; i++) {
      _x = this.p[i].x * 20 + this.x;
      _y = this.p[i].y * 20 + this.y;
      ret.push({x:_x, y:_y, col:this.c})
    }
    return ret;
  }



} // class
