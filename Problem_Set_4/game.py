import random

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass

def get_quess(level):
    while True:
        try:
            g = int(input("Guess: "))
            if g in range(1, level+1):
                return g
        except ValueError:
            pass

def guess_game(level):
    ans = random.randint(1,level)
    while True:
        g = get_quess(level)
        if g == ans:
            print("Just right!")
            break
        elif g < ans:
            print("Too small!")
            continue
        else:
            print("Too large!")
            continue


level = get_level()
guess_game(level)
