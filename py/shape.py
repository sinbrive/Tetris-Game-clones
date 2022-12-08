from tetrominoes import *
import random
 
tetrominoes=[t_I, t_O, t_J, t_L, t_S, t_Z, t_T]  

colrs=['#ff0000','#00ff00','#0000ff','#ffff00',  
                                '#ff00ff','#00ffff', '#fffefe'] 


class Shape:
  def __init__(self, x=10, y=10):
    self.x = x
    self.y = y
    self.rotIndex=0
    self.pattern=random.choice(tetrominoes)
    self.p = self.pattern[self.rotIndex]
    self.c =colrs[tetrominoes.index(self.pattern)]
  

  def getXoffset(self):
    return self.x
  

  def getYoffset(self):
    return self.y
  
  
  def setXoffset(self,x):
    self.x=x
  

  def setYoffset(self,y):
    self.y=y
  

  def rotate(self, rot):
    self.rotIndex=rot
    self.p = self.pattern[self.rotIndex]
  
  
  def getPattern(self):
    return self.p
  

  def getColor(self):
    return self.c
  

  def move(self, x, y):
    self.x += x
    self.y += y
  
  
  def draw(self):
    fill(self.c)
    for i in range(len(self.p)):
      s = self.p[i]
      x = s.x * 20 + self.x
      y = s.y * 20 + self.y
      rect(x, y, 20, 20)
    
  

  def maxY(self):
    return max([o.y for o in self.p])
  

  def getNbX(self):
    return max([o.x for o in self.p])+1

  def xOutRightSide(self,limit):
    for i in range(len(self.p)):
      s = self.p[i]
      x= s.x*20+self.x
      if x>limit: 
        return True
    return False
  

  def canMoveDown(self, wall):
    for i in range(len(wall)):
      ln = wall[i]
      for j in range(4):
        a = self.p[j].x * 20 + self.x
        b = self.p[j].y * 20 + self.y
        if (a == ln.x) and (b == ln.y): 
          return False
    return True

  def highestY(self):
      return (self.y + 20 * self.maxY())
  

  def getRealCoords(self):
    ret=[]
    p=None
    _x=0
    _y=0

    for i in range(len(self.p)):
      _x = self.p[i].x * 20 + self.x
      _y = self.p[i].y * 20 + self.y
      p = Point(_x, _y, self.c)
      ret.append(p)
    
    return ret
  
