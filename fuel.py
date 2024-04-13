def main():
    fraction = str(input("Fraction: "))
    perc = convert(fraction)
    s = gauge(perc)
    if type(perc) == int:
        print(s)

def convert(fraction):
    try:
        if "/" not in fraction:
            raise ValueError
        frac = fraction.split("/")
        x = int(frac[0])
        y = int(frac[1])
        perc = int(round((x/y) * 100, 0))
        if perc > 100 or perc < 0:
            raise ValueError
        else:
            return perc
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide with zero!")
    except ValueError:
        raise ValueError("Input Format: (int)/(int)")


def gauge(perc):
    try:
        if perc >= 99:
            return "F"
        elif perc <= 1 and perc >= 0:
            return "E"
        else:
            return f"{perc}%"
    except TypeError:
        raise TypeError("Input is not an integer Percentage")


if __name__ == "__main__":
    main()
