import turtle
import random
from playsound import playsound
import pygame
pygame.init()
pygame.mixer.init()
sound1 = pygame.mixer.Sound("Audio/m1.mp3")
sound2 = pygame.mixer.Sound("Audio/m2.wav")
b = turtle.Turtle()
turtle.register_shape('basket.gif')
turtle.register_shape('fr1.gif')
turtle.register_shape('fr2.gif')
turtle.register_shape('fr3.gif')
turtle.register_shape('fr4.gif')
b.shape('basket.gif')
t = turtle.Screen()
t.setup(width = 850, height = 850) 
turtle.bgpic("tree.gif")
t.tracer(0.1)
t.title("fruit basket")
b.shapesize(100,200,200)
b.penup()
b.goto(0,-370)           
#x = random.randint(-375, 375)  
#y = random.randint(-375, 375)
o = turtle.Turtle()
colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])


#o.color(colors)
o.shape(shapes)

o.right(90)
o.penup()



o1 = turtle.Turtle()
colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])
#o1.color(colors)
o1.shape(shapes)
o1.penup()

o1.right(90)
o1.penup()

bomb1 = turtle.Turtle()
turtle.register_shape('bomb.gif')
bomb1.shape('bomb.gif')
bomb1.penup()
bomb1.right(90)
bomb1.goto(350,450)

pen1 = turtle.Turtle()  
pen1.speed(0)  
pen1.shape("square")  
pen1.color("#00ffff")  
pen1.penup()  
pen1.hideturtle()  
pen1.goto(-100,370)  
pen1.write("Score: 0, High Score: 0", align = "right",  
          font = ("Consoles", 22, "bold"))  
is_paused = False

def pause():
   global is_paused
   if is_paused == True:
       is_paused = False
   else:
       is_paused = True    
def goleft():
   b.setheading(180)
def goright():
   b.setheading(0)

    

t.onkeypress(goleft, "Left")  
t.onkeypress(goright, "Right") 
t.onkeypress(pause, "space")
t.listen()
spawn = 1
score = 0  
high_score = 0
#question = input("wanna play game")
#if question=="yes":
while spawn==1:
      if not is_paused:   
          o.forward(0.3)
          o1.forward(0.3)
          bomb1.forward(0.3)
          
          if b.distance(bomb1) < 70:
              #playsound('Audio/m1.mp3')
              sound1.play()
              spawn+=1
          elif bomb1.ycor() < -425:
                j = random.randint(-375, 375)  
                k = random.randint( 425, 525 ) 
                bomb1.goto(j,k) 
          if b.distance(o) < 20:
              pen1.clear()
              #playsound('Audio/m2.wav')
              sound2.play()
              score += 10
              if score > high_score:  
                high_score = score  
              pen1.write("Score : {} High Score : {} ".format(score,high_score), align = "center", font = ("Consoles", 22, "bold"))     
              x = random.randint(-375, 375)  
              y = random.randint( 425, 525 )  
              colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
              shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])

              o.color(colors) 
              o.shape(shapes)
              o.goto(x, y)
          elif o.ycor() < -425:
             x = random.randint(-375, 375)  
             y = random.randint(425, 525)
             colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
             shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])

             o.color(colors) 
             o.shape(shapes)
             o.goto(x,y)    
          
          if b.distance(o1) < 20:             
              pen1.clear()
              #playsound('Audio/m2.wav')
              sound2.play()
              score += 10
              if score > high_score:  
                 high_score = score 
              pen1.write("Score : {} High Score : {} ".format(  
              score,high_score), align = "center", font = ("Consoles", 22, "bold"))  
              w = random.randint(-375, 375)  
              q= random.randint(425, 525)  
              colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
              shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])

              o1.color(colors) 
              o1.shape(shapes)
          
              o1.goto(w, q) 
          elif o.ycor() < -425:
             w = random.randint(-375, 375)  
             q = random.randint(425, 525)
             colors = random.choice(['pink', 'magenta', 'blue','green','red','purple'])
             shapes = random.choice([ 'fr1.gif','fr2.gif','fr3.gif','fr4.gif'])

             o1.color(colors) 
             o1.shape(shapes)
             o1.goto(w,q)    
          if b.xcor()<375:
             b.forward(0.3)
          else:
             b.setheading(180)
             b.forward(0.3)   
          if b.xcor()>-375:
              b.forward(0.3)
          else:
             b.setheading(0)
             b.forward(0.3)             
          t.update() 
      else:
          t.update()      
turtle.mainloop()



