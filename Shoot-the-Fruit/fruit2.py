# Gmae : Shoots-the-fruits
import pgzrun
from random import randint
#define size windoes
WIDTH = 640
HEIGHT = 480

#ctreate object
apple = Actor('apple')

# function for display
def draw():
  score1 = 0
  screen.clear()
  screen.fill ((80,135,255))
  for n in range(5):
    place_apple()
    apple.draw()
  
 


# function random
def place_apple() :
  apple.x = randint(10,600)
  apple.y = randint(10,400)


 
#function get event mouse
def on_mouse_down(pos):
  print(pos)
  sounds.click.play()
  if apple.collidepoint(pos):
    print("Good Shot")
    place_apple()
  else:
    print("You are missed")
   
   
          
 
place_apple()
pgzrun.go()
