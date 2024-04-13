def main():
    #Input time in format ##:##
    x = str(input("What time is it? "))
    x = convert(x)
    if x >= 7 and x <= 8:
        print("breakfast time")
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 18 and x <= 19:
        print("dinner time")

def convert(time: str):
    time = time.split(":")
    return int(time[0]) + int(time[1])/60.0

if __name__ == "__main__":
    main()