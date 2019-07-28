# Gmae : Shoots-the-fruits
import pgzrun
from random import randint
#define size windoes
WIDTH = 640
HEIGHT = 480
score = 0
time_count = 0
timer = 0
game_over = False
#ctreate object
apple = Actor('apple')
pineapple = Actor('pineapple')
orange = Actor('orange')

# function for display
def draw():
  global score
  screen.clear()
  screen.fill ((80,135,255))
  apple.draw()
  pineapple.draw()
  orange.draw()
  screen.draw.text("Score : "+str(score),color = 'black', topleft=(550,10))
  screen.draw.text("Time : "+str(timer),color = 'black', topleft=(10,10))
  
  if game_over:
    screen.fill('black')
    message = "Final Score : " +str(score)
    screen.draw.text(message, topleft=(280,150), fontsize = 50)



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
  global score

  if apple.collidepoint(pos):
    print("Good Shot")
    sounds.click.play()
    place_apple()
    score += 2
  
  if pineapple.collidepoint(pos):
    print("Good Shot")
    sounds.click.play()
    place_pineapple()
    score += 1

  if orange.collidepoint(pos):
    print("Good Shot")
    sounds.click.play()
    place_orange()
    score +=1
def update():
  apple.y += 2
  orange.y +=2
  pineapple.y +=2
  if apple.y > HEIGHT:
    apple.y = 0
  if pineapple.y > HEIGHT:
    pineapple.y = 0
  if orange.y > HEIGHT:
    orange.y = 0
def time_up():
  global game_over
  game_over = True
  
def time_count():
  global timer
  timer +=1

clock.schedule(time_up, 10.0)
clock.schedule_interval(time_count ,1.0)
  
place_apple()
place_pineapple()
place_orange()
pgzrun.go()
