import turtle, random


t=turtle.Turtle()
s=turtle.Screen()

t.speed(0)

color=["red","green","blue","pink","orange","cyan"]

ch=random.choice(color)

t.color(ch)

r=int(turtle.textinput("원크기", "원의 반지름 입력: "))
num1=int(turtle.textinput("꽃잎수", "원의 갯수: "))


for i in range(num1):
    t.circle(r)
    t.left(360/num1)
    
t.color(random.choice(color))
r1=random.randint(30,100)
num2=random.randrange(4,11,2)

for i in range(num2):
    t.circle(r1, 360 ,4)
    t.left(360/num2)



s.mainloop()
