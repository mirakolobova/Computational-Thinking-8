import turtle, time, random
from utils import *
#Controls
#J = Job, you lose 1 happiness and get 1 dollar
#F = food, you get food for 1 dollar and gain 1 happiness
#E = entertainment, you get entertainment for 1 dollar and gain 1 happiness
#Goal
#Don't let your character have no money and no happiness



# Section 1 - setup
# TODO - set a background using set_background()
set_background("barn")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
money = 10
food = 0
entertainment = 0
happiness = 100
message_sprite = create_sprite("alien", -300,200)
message_sprite.hideturtle()
create_sprite("person", 50,50)


# Section 2 - controls
# TODO - define an action. ex: def my_control()

def make_money():
    global money, happiness
    money += 1
    happiness -= 1
window.onkeypress(make_money, "j")

def get_entertainment():
    global entertainment, happiness, money
    if money >= 1:
        entertainment += 1
        happiness += 1
        money -= 1
        x = random.randint (-200,200)
        y = random.randint (-200,200)
        p1 = create_sprite("phone",x,y)
        time.sleep(0.5)
        p1.hideturtle()
    elif money <= 1:
        print("You can't afford this!")

window.onkeypress(get_entertainment, "e")

def get_food():
    global food, happiness, money
    if money >= 1:
        food += 1
        happiness += 1
        money -= 1
        x = random.randint (-200,200)
        y = random.randint (-200,200)  
        p1 = create_sprite("steak",x,y)
        time.sleep(0.5)
        p1.hideturtle()

    elif money <= 1:
        food += 0
        happiness += 0
        print("You can't afford this!")
window.onkeypress(get_food, "f")

def get_money():
    global money, happiness
    money += 1
    happiness -= 1
window.onkeypress(get_money, "j")
    


# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"Food: {food}\nEntertainment: {entertainment}\nMoney: {money}\nHappiness: {happiness}")

    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()