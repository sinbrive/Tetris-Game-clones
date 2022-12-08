from game import Game

game=None

#------------------
def setup():
  global game
  size(200+100, 400)
  game = Game()
  game.setup()


#------------------
def draw():
  background(0)
  game.update()
  game.draw()



#------------------
def keyPressed():
  if key==CODED:
    game.inputKey(keyCode)
