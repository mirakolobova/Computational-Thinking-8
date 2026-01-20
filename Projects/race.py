import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 250
x2 = -250
y2 = 150
x3 = -250
y3 = 50
x4 = -250
y4 = -50



# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("Raccoon",x1,y1)
t2 = create_sprite("bettercrow",x2,y2)
t3 = create_sprite("fox",x3,y3)
t4 = create_sprite("dog",x4,y4)
# comment
print("The crow is most likely to win because they are the fastest and most consistent. The raccoon has potential to beat them but most likely won't. The fox will come in 3rd and the dog will come in 4th.")
time.sleep(2)
# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    x1 += random.randint(1,25)
    x2 += 16
    x3 += 13
    x4 += 11

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")
turtle.exitonclick()