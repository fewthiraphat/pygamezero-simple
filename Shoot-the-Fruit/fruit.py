# Gmae : Shoots-the-fruits
import pgzrun
from random import randint
#define size windoes
WIDTH = 640
HEIGHT = 480

#ctreate object
apple = Actor('apple')
pineapple = Actor('pineapple')
orange = Actor('orange')
# function for display
def draw():
  score1 = 0
  screen.clear()
  screen.fill ((80,135,255))
  
  apple.draw()
  pineapple.draw()
  orange.draw()
 


# function random
def place_apple() :
  apple.x = randint(10,600)
  apple.y = randint(10,400)

def place_pineapple() :
  pineapple.x = randint(10,600)
  pineapple.y = randint(10,400)
  
def place_orange() :
  orange.x = randint(10,600)
  orange.y = randint(10,400)
 
#function get event mouse
def on_mouse_down(pos):
  print(pos)
  sounds.click.play()
  if apple.collidepoint(pos):
    print("Good Shot")
    place_apple()
    
  elif pineapple.collidepoint(pos):
    print("Good Shot")
    place_pineapple()
    

  elif orange.collidepoint(pos):
    print("Good Shot")
    place_orange()
  else:
    print("You are missed")
#define update score
def update():
  if place_apple
    fox.score = fox.score +1
  elif place_pineapple()
    fox.score = fox.score +1
   
          
 
place_apple()
place_pineapple()
place_orange()
pgzrun.go()
