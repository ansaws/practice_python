from random import randrange
g = ["rock", "paper", "scissor"]
c = 0
p = 0
while True:
    x = input("Press r for rock, p for paper and s for scissors: ")
    y = randrange(1,4)
    print("The computer played,", g[y-1])
    #computer plays rock
    if y == 1:
        if x == 'p':
            p += 1
            print("You won you get one point. You have", p, "points. The computer has", c, "points.")
        elif x == 's':
            c+=1
            print("You lost, computer gets one point. You have", p, "points. The computer has", c, "points.")
        elif x == 'r':
            print("Draw no one gets a point. You have", p, "points. The computer has", c, "points.")
    #computer plays paper
    if y ==2:
        if x == 's':
            p += 1
            print("You won you get one point. You have", p, "points. The computer has", c, "points.")
        elif x == 'r':
            c+=1
            print("You lost, computer gets one point. You have", p, "points. The computer has", c, "points.")
        elif x == 'p':
            print("Draw no one gets a point. You have", p, "points. The computer has", c, "points.")
    #computer plays scissor
    if y ==3:
        if x == 'r':
            p += 1
            print("You won you get one point. You have", p, "points. The computer has", c, "points.")
        elif x == 'p':
            c+=1
            print("You lost, computer gets one point. You have", p, "points. The computer has", c, "points.")
        elif x == 's':
            print("Draw no one gets a point. You have", p, "points. The computer has", c, "points.")
    b = int(input("do you want to continue playing press 0 for yes and 1 for no: "))
    if b  == 0:
        pass
    elif b ==1:
        if c>p:
            print("sorry you lost, play agian another time.")
        if p>c:
            print("Great Job you won :), play again another time.")
        break