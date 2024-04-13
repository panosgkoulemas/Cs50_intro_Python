import random
    

def main():
    level = get_level()
    correct = 0
    for _ in range(0,10):
        a = generate_integer(level)
        b = generate_integer(level)
        count = 0
        while True:
            try:
                result = int(input(f"{a} + {b} = "))
                if a + b != result:
                    print("EEE")
                    count = count + 1
                    if count == 3:
                        print(f"{a} + {b} = {a+b}")
                        break
                else:
                    correct = correct + 1
                    break
            except ValueError:
                print("EEE")
                count = count + 1
                if count == 3:
                    print(f"{a} + {b} = {a+b}")
                    break
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()