from random import * #import everthing from the random module
from turtle import * #import everything from the turtle module
from freegames import vector #imports only vector from the freegames module
bird = vector(0,0)
balls = []

def tap(x, y): #defines a function that moves the bird when the screen is tapped
  up = vector(0, 30) #Move the birds position by the defined upward vector
  bird.move(up) #mobve the birds position by the defined upward vector

def inside(point):
  return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
  clear()

  goto(bird.x, bird.y)   #moves the turtle to the birds position

  if alive:    #draws the bird as a green dot if its alive or otherwise a red dot if it is not
    dot(10, 'green')
  else:
    dot(10, 'red')

  for ball in balls:
    goto(ball.x, ball.y)
    dot(20, 'black')

  update()

def move(): # defines a function that updates the objects positions
  bird.y -= 5
  for ball in balls: # moves each falling ball left by 3 
    ball.x -= 3
  if randrange(10) == 0:   #Randomly creates a new falling ball with a y coord within the given range
    y = randrange(-199, 199)
    ball = vector(199, y)
    balls.append(ball)

  while len(balls) > 0 and not inside(balls[0]):
    balls.pop(0)

  if not inside(bird):  # Checks if the bird is outside the screens boundries, draws the screen accordingly and then returns IF its not alive
    draw(False)
    return

  for ball in balls:
    if abs(ball - bird) < 15:
        draw(False)
        return

  draw(True)
  ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
