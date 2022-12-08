from shape import Shape

class Game:
  def __init__(self):
    self.rotIndex = 0  
    self.lines = [] 
    self.score = 0
    self.points_per_level=100
    self.level=1
    self.game_over = False
    self.chrono=millis()
    self.timeLevel=1000
    self.shape= None
    self.nextShape = None
  

  def setup(self):
    rectMode(CENTER)
    self.shape = Shape(10,10)
    self.nextShape = Shape(width-70, 50)
  

  def update(self):
    if (self.game_over): return
    self.makeStepDown()
    if (not self.shape.canMoveDown(self.lines) or self.nextOnFloor()): 
      self.shape.move(0, -20)
      self.lockCurrentShape()  
      self.switchToNextShape()
      self.checkUpdateScore()
      
    

  def draw(self):
    self.displayGrid()
    self.shape.draw()
    self.drawLines()
    self.displaySideBoard()
    if (self.game_over):
        fill(255,100,100)
        text("Game Over", width-70, height/2+150)

  
  def makeStepDown(self): 
    if (millis() - self.chrono > self.timeLevel):
      self.chrono = millis()
      self.shape.move(0, 20)
    

  def nextOnFloor(self):
    return not (self.shape.highestY() < height)
  
  
  def switchToNextShape(self):
    self.rotIndex = 0
    self.chrono = millis()
    self.shape = self.nextShape
    self.shape.setXoffset(10)
    self.shape.setYoffset(10)
    self.nextShape = Shape(width-70, 50)
  

  def displaySideBoard(self):
    fill('#222222')
    rect(width-50, height/2, 100, 400)
    self.nextShape.draw()
    fill(130)
    textSize(15)
    text("Level "+str(self.level), width-80, height/2)
    text("Score "+str(self.score), width-80, height/2+50)
  

  def displayGrid(self):
    noFill()
    stroke(180)
    strokeWeight(0.1)
    for y in range(10, 400, 20):
      for x in range(10, 200, 20):
        rect(x, y, 20, 20)
      
    
  

  def lockCurrentShape(self):  
    arr = self.shape.getRealCoords()
    for i in range(len(arr)):
      self.lines.append(arr[i])
    
  def checkUpdateScore(self):
    for i in range(len(self.lines)):
      row = 400 - i * 20 - 10
      count=0
      for item in self.lines:
        if item.y == row:
          count+=1
      if count == 10:
        self.removeLine(row)
        self.score+=20
        if self.score > self.points_per_level*self.level:
          self.score=0
          self.level+=1
    for item in self.lines:
      if item.y < 30:
        self.game_over= True
        return
  

  def removeLine(self,row):
    self.lines = list(filter(lambda item: item.y != row, self.lines))
    for i in range(len(self.lines)):
      ln = self.lines[i]
      if ln.y < row:
        ln.y += 20
        self.lines[i].y = ln.y
    
  

  def drawLines(self):
    for i in range(len(self.lines)):
      ln = self.lines[i]
      fill(ln.c)
      rect(ln.x, ln.y, 20, 20)
    
  

  def inputKey(self,key):

    x=0
    y=0

    if (key == RIGHT):
      x = self.shape.getXoffset()
      if (x < width-100 - 20 * self.shape.getNbX()): self.shape.move(20,0)
    
  
    if (key == LEFT):
      x= self.shape.getXoffset()
      if x > 20: self.shape.move(-20,0)
    
    
    if (key == DOWN):
      y=self.shape.getYoffset()
      if (y < height-20): self.shape.move(0,20)
    
  
    if (key == UP):
      save =self.rotIndex
      self.rotIndex+=1
      self.rotIndex = self.rotIndex % 4
      # disable rotation to prevent overflow
      self.shape.rotate(self.rotIndex)
      if (self.shape.xOutRightSide(width-100)):
        self.rotIndex = save
      
      self.shape.rotate(self.rotIndex)
       
