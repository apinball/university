import turtle

t=turtle.Turtle()
s=turtle.Screen()

name=turtle.textinput("이름입력", "이름을 입력하시오: ")
t.write("안녕하세요. "+name+"님, 좋은 저녁입니다.")

for i in range(3):
    t.left(360/3)
    t.fd(100)


t.fd(300)
t.begin_fill()
t.fillcolor("red")
t.circle(20)
t.end_fill()

s.mainloop()
