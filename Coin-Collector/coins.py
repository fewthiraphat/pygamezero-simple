import pgzrun
from random import randint

#define size windows
WIDTH = 800
HEIGHT = 600
#define variable
score = 0
game_over = False
timer = 0
#create_object
fox = Actor('fox')
fox.pos = 100,100

coin = Actor('coin')
coin.pos = 200,200

hedgehog = Actor('hedgehog')
hedgehog.pos = 770,570


#วาด
def draw(): 
  screen.fill('green')
  fox.draw()
  coin.draw()
  hedgehog.draw()
  
  screen.draw.text("Score : "+str(score), color='black', topleft=(10,10))
  screen.draw.text("Time : "+str(timer), color='black', topright=(750,10))
  if game_over:
    screen.fill('pink')
    message = "Final Score : " +str(score)
    screen.draw.text(message, topleft=(350,250), fontsize = 50)
    
    
#เหรียญ
def place_coin():
  coin.x = randint(20, (WIDTH - 20))
  coin.y = randint (20, (HEIGHT - 20))
  
#Keyboard
def update():
  global score
  if keyboard.left:
    fox.x = fox.x - 5
  elif keyboard.right:
    fox.x = fox.x +5
  elif keyboard.up:
    fox.y = fox.y -5
  elif keyboard.down:
    fox.y = fox.y +5
    
  coin_collected = fox.colliderect(coin)
  if coin_collected:
    place_coin()
    score += 1

def time_up():
    global game_over
    game_over = True

def time_count():
    global timer
    timer += 1

clock.schedule(time_up, 30.0)
clock.schedule_interval(time_count, 1.0)
place_coin()
pgzrun.go()
