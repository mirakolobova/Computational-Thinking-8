dog_points = 0
cat_points = 0
fish_points = 0
answer1 = input("Do you prefer A; Big animals B; Medium animals C; Small animals    ")
if answer1 == "A":
    dog_points += 1
elif answer1 == "B":
    cat_points += 1
elif answer1 == "C":
    fish_points += 1

answer2 = input("Do you prefer A; Fluffy B; Not fluffy      ")
if answer2 == "A":
    dog_points += 1
    cat_points += 1
elif answer2 == "B":
    fish_points += 1

answer3 = input("What can you handle? A High maintenance B Low maintenance      ")
if answer3 == "A":
    dog_points += 1
    cat_points += 1
elif answer3 == "B":
    fish_points += 1

answer4 = input("Can this pet be loud? A; Yes B; No        ")
if answer4 == "A" or answer4 == "D":
    dog_points += 1
elif answer3 == "B":
    cat_points += 1
    fish_points += 1

answer5 = input("What is your favorite animal out of these? A; Dog B; Cat C; Fish       ")
if answer5 == "A":
    dog_points += 1
    cat_points -= 1
    fish_points -= 1
elif answer5 == "B":
    cat_points += 1
    fish_points -= 1
    dog_points -= 1
elif answer5 == "C":
    fish_points += 1
    cat_points -= 1
    dog_points -= 1

print(f"Here are your points: dog {dog_points}, cat {cat_points}, fish {fish_points}")

if dog_points >= cat_points and dog_points >= fish_points:
    print("You are a dog person")
elif fish_points >= cat_points and fish_points >= dog_points:
    print("You are a fish person")
elif cat_points >= dog_points and cat_points >= fish_points:
    print("You are a cat person")
else:
    print("You are tied")