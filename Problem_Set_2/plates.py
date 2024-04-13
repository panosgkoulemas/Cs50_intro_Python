def main():
    plate = str(input("Plate: ")).upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    count = 0
    if len(s) < 2 or len(s) > 6:
        return False
    if (s[0].isalpha() and s[1].isalpha()) == False:
        return False
    for char in s[2:]:
        if char.isalnum() == False:
            return False
    for i in range(2, len(s)-1):
        if s[i].isdigit() and (s[-1].isdigit() == False):
            return False
        #If first digit is zero
        elif count == 0 and s[i] == '0':
             return False
        elif s[i].isdigit():
            count = count + i
    #Numbers in the list is the sum of the indexes of the input string
    #For consecutive positions of digits from the 2nd to the 4th index(0,1,2,3,4,5)
    #0: No digits at all
    #4: if only last two chars are digits
    #7: if last three chars are digits
    #9: if last four chars are digits
    if len(s) == 6 and (count not in [0, 4, 7, 9]):
            return False
    if len(s) == 5 and (count not in [0, 3, 5]):
            return False
    if len(s) == 4 and (count not in [0, 2]):
            return False
    else:
        return True


main()