
let tetrominoes=[I, O, T, J, L, S, Z];  

let colrs=['#00ffff','#ffff00','#800080','#00ff00',  
                                '#ff0000','#0000ff', '#ffA500'];

class Shape {
  constructor(x, y) {
    this.x = x || 10;
    this.y = y || 10;
    this.p=random(tetrominoes);
    this.c =colrs[tetrominoes.indexOf(this.p)];
    this.rotationTick=millis()
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

  rotate(limit){
    if ((millis()-this.rotationTick) < 300) return;
    this.rotationTick=millis()
    let sh = this._transpose(this.p);
    sh = this._reverse(sh);
    if (this.xOutRightSide(sh, limit)) return;
    this.p = sh;
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
    let sh = this.p;
    for (let y = 0; y < sh.length; y++) {
      for (let x = 0; x < sh[0].length; x++) {
        if (sh[y][x] == 1) {
          rect(20 * x + this.x, 20 * y + this.y, 20, 20)
        }
      }
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
    return this.p[0].length;
  }

 xOutRightSide(sh, limit){
    // let sh = this.p;
    for (let y = 0; y < sh.length; y++) {
        if (sh[y][sh[0].length-1] == 1) {
          let x = 20*(sh[0].length-1)+this.x
          if (x > limit) return true        
        }
      }
   return false;
 }

 canMoveDown(wall){
  for (let i = 0; i < wall.length; i++) {
    let ln = wall[i];
    let sh = this.p;
    for (let y = 0; y < sh.length; y++) {
          for (let x = 0; x < sh[0].length; x++) {
            if (sh[y][x] == 1) {
              let a = x * 20 + this.x;
              let b = y * 20 + this.y;
              if ((a == ln.x) &&
                (b == ln.y)) return false;
            }
          }
        }
  }
  return true;
}


highestY(){
  return (this.y + 20 * (this.p.length-1))
}

getRealCoords(){
  let ret=[];
  let x, y;
  let sh = this.p;
  for (let y = 0; y < sh.length; y++) {
    for (let x = 0; x < sh[0].length; x++) {
      if (sh[y][x] == 1) {
        let a = x * 20 + this.x;
        let b = y * 20 + this.y;
        ret.push({x:a, y:b, col:this.c})
      }
    }
  }
  return ret;
}

_transpose(sh){
  return sh[0].map((col, c) => sh.map((row, r) => sh[r][c]));
 }

   
 _reverse(sh) {
   return sh.map(function(ar){return ar.reverse();});
 }



} // class
