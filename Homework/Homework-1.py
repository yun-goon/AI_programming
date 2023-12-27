import turtle as t

t.speed(0)
t.setup(width=400, height=400)
t.screensize(0,0,'skyblue') # 바탕 하늘

def draw_sun(r, c): #반지름, 색
    t.color(c)
    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def moving(x,y): #위치로 이동
    t.up()
    t.home()
    t.setpos(x,y)
    t.pd()


def mount(x,y,s,c): #좌표, 크기, 색
    moving(x,y)
    t.color(c)
    t.fillcolor(c)
    t.begin_fill()
    t.left(60)
    t.forward(s)
    t.right(120)
    t.forward(s)
    t.right(120)
    t.forward(s)
    t.end_fill()


# 태양
moving(40,5-120)
draw_sun(180,'purple')
moving(40,20-120)
draw_sun(160, 'pink')
moving(40,45-120)
draw_sun(140, 'red')
moving(40,60-120)
draw_sun(120, 'orange')
moving(40,85-120)
draw_sun(80, 'yellow')

#풀
moving(-200,0)
t.fillcolor('green')
t.begin_fill()
t.forward(400)
t.left(90)
t.forward(-190)
t.left(90)
t.forward(400)
t.end_fill()

#산
mount(-250,-80,200,'white')
mount(-100,-80,250,'white')
mount(0,-80,200,'white')

mount(-300,-100,200,'dark gray')
mount(-150,-100,200,'dark gray')
mount(-10,-90,180,'dark gray')
mount(80,-90,200,'dark gray')

mount(-250,-150,200,'gray')
mount(-100,-100,100,'gray')
mount(-50,-150,150,'gray')

#길
moving(100,-200)
t.color('dark orange')
t.fillcolor('dark orange')
t.begin_fill()
t.left(40)
t.forward(30)
t.left(40)
t.forward(30)
t.left(40)
t.forward(30)
t.left(40)
t.forward(30)
t.right(90)
t.forward(10)
t.right(90)
t.forward(40)
t.right(40)
t.forward(40)
t.right(40)
t.forward(40)
t.right(40)
t.forward(40)
t.end_fill()

t.done()