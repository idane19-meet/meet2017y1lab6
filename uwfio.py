import turtle
speed = 0.5
def speed_f():
    global speed
    speed = speed + 0.5
turtle.onkeypress(speed_f, "space")
turtle.listen()
while True:
    turtle.forward(speed)
turtle.mainloop()
