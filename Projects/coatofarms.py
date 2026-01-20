# Section 1 - Your code
from utils import *
set_background("green")

s1 = create_sprite("Raccoon", 275, -225)
s2 = create_sprite("bettercrow", -300, 200)
s3 = create_sprite("cardinal", -100, -100)
s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-50 ,200)
message1.color("black")
message1.write("Mira",font = ("Impact", 40, "bold"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()