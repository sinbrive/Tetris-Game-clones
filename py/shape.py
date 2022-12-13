from tetrominoes import *
import random
 
tetrominoes=[I, O, T, J, L, S, Z] 

colrs=['#00ffff','#ffff00','#800080','#00ff00',  
                                '#ff0000','#0000ff', '#ffA500'] 


class Shape:
  def __init__(self, x=10, y=10):
    self.x = x
    self.y = y
    self.p=random.choice(tetrominoes)
    self.c =colrs[tetrominoes.index(self.p)]
    self.rotationTick=millis()
  

  def getXoffset(self):
    return self.x
  

  def getYoffset(self):
    return self.y
  
  
  def setXoffset(self,x):
    self.x=x
  

  def setYoffset(self,y):
    self.y=y
  

  def rotate(self, limit):
    if (millis()-self.rotationTick) < 300: return
    self.rotationTick=millis()
    sh = self._transpose(self.p)
    sh = self._reverse(sh)
    if self.xOutRightSide(sh, limit): return
    self.p = sh
  
  
  def getPattern(self):
    return self.p
  

  def getColor(self):
    return self.c
  

  def move(self, x, y):
    self.x += x
    self.y += y
  
  
  def draw(self):
    fill(self.c)
    sh = self.p
    for y in range(len(sh)):
      for x in range(len(sh[0])): 
        if sh[y][x] == 1:
          rect(20 * x + self.x, 20 * y + self.y, 20, 20)
  
  def getNbX(self):
    return len(self.p[0])

  def xOutRightSide(self, sh, limit):
    for y in range(len(sh)):
      if sh[y][len(sh[0])-1] == 1:
          x = 20*(len(sh[0])-1)+self.x
          if x > limit: return True        
    return False

  def canMoveDown(self, wall):
    sh = self.p
    for i in range(len(wall)):
        ln = wall[i]
        for y in range(len(sh)):
            for x in range(len(sh[0])):
                if sh[y][x] == 1:
                    a = x * 20 + self.x
                    b = y * 20 + self.y
                    if a == ln.x and b == ln.y:
                        return False
    return True

  def highestY(self):
      return self.y + 20 * (len(self.p)-1)

  def getRealCoords(self):
    ret=[]
    sh = self.p
    for y in range(len(sh)):
      for x in range(len(sh[0])): 
        if sh[y][x] == 1:
          a = x * 20 + self.x
          b = y * 20 + self.y
          p = Point(a, b, self.c)
          ret.append(p)
    return ret

  def _transpose(self, sh):
    # sh = self.p
    # ret = [ [0]*len(sh) for i in range(len(sh[0]))]
    # for i in range(len(sh)):
    #     for j in range(len(sh[0])):
    #         ret[j][i]=sh[i][j]
    # return ret
    return [list(i) for i in zip(*self.p)]
  

  def _reverse(self, sh):
    return sh[::-1]
  
