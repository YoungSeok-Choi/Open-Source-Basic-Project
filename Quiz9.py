import turtle
import random
import sqlite3
import time

swidth, sheight, psize, exitcount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7
turtlepath = sqlite3.connect("turtleDB.db")  # 경로재설정
csr = turtlepath.cursor()


# DB 생성 안되있다면 주석풀기
csr.execute("CREATE TABLE usertable (선분ID int, 색상R float, 색상G float, 색상B float, 순번 int, X좌표 int, Y좌표 int)")


turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(psize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

number = 1

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()
    print("첫번째 와일문의 앵글 디스트 값\n")
    print("%d" % angle)
    print(" %d\n" % dist)

    sql = "INSERT INTO usertable VALUES('" + str(number) + "','" + str(r) + "','" + str(g) + "','" + str(b) + "','" + str(number) + "','" + str(curX) + "'," + str(curY) + ")"
    number += 1
    turtlepath.execute(sql)
    turtlepath.commit()


    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitcount += 1
        if exitcount >= 5:
            break


turtle.home()
time.sleep(10) #photo time

Turtle = turtle
Turtle.title("거북이가 거꾸로 다니기")
Turtle.shape('turtle')
Turtle.pensize(psize)
Turtle.setup(width=swidth + 30, height=sheight + 30)
Turtle.screensize(swidth, sheight)


sql1 = "SELECT * from usertable"
csr.execute(sql1)
Turtle.clear()

exitcount = 0
print("\n===============================================================================================================================\n")
for row in csr:
    r = float(row[1])
    g = float(row[2])
    b = float(row[3])

    turtle.pencolor((r, g, b))

    #angle = random.randrange(0, 360)
    #dist = random.randrange(1, 100)
    #turtle.left(angle)
    #turtle.forward(dist)
    #curX = float(row[5])
    #curY = float(row[6])

    curX = int(row[5])
    curY = int(row[6])
    print("\n두번째 와일문의 디비출력 앵글 디스트 값\n")
    print("%d" % row[5])
    print(" %d\n" % row[6])
    turtle.goto(curX, curY)



    if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitcount += 1
        if exitcount >= 5 :
            break


turtle.home()
time.sleep(10) #photo time

turtle.done
turtlepath.close()