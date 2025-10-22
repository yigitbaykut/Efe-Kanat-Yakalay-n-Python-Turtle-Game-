import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Efe Kanat'ı Yakalayın!")
EfeKanat = turtle.Turtle()

drawing_board.addshape("efekanat2.gif")
EfeKanat.shape("efekanat2.gif")

EfeKanat.penup()

EfeKanat.speed(1)

EfeKanat.shapesize(stretch_wid=10, stretch_len=10)


score = 0
moves = 15

scoreboard = turtle.Turtle()
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-30,300)
scoreboard.write("Score:", align="center", font=("Arial", 24, "bold"))



count = turtle.Turtle()
count.color("black")
count.penup()
count.hideturtle()
count.goto(30,300)
count.write(f"{score}", align="center", font=("Arial", 24, "bold"))


efe_sayi = turtle.Turtle()
efe_sayi.color("black")
efe_sayi.penup()
efe_sayi.hideturtle()
efe_sayi.goto(0,340)
efe_sayi.write("Efe Kanat's left:", align="center", font=("Arial", 20, "bold"))

efe_count = turtle.Turtle()
efe_count.color("black")
efe_count.penup()
efe_count.hideturtle()
efe_count.goto(90,340)



def fxn(x, y):
    global score
    score += 1
    count.clear()
    count.write(f"{score}", align="center", font=("Arial", 24, "bold"))


EfeKanat.onclick(fxn)


def move_randomly():
    global moves
    if moves > 0:
        EfeKanat.hideturtle()
        ranx = random.randint(-250, 250)
        rany = random.randint(-250, 250)
        EfeKanat.goto(ranx, rany)
        EfeKanat.showturtle()
        moves -= 1
        drawing_board.ontimer(move_randomly, 500)
        efe_count.clear()
        efe_count.write(f"{moves}", align="center", font=("Arial", 20, "bold"))
    else:
        end = turtle.Turtle()
        end.hideturtle()
        end.color("red")
        end.write("Oyun Bitti!", align="center", font=("Arial", 36, "bold"))
        EfeKanat.onclick(None)



move_randomly()

turtle.mainloop()