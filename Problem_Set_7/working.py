#Formats: {1} 9 AM to 5 PM {2} 9:00 AM to 5:00 PM    
#Converted to: 9:00 to 17:00
import re
import sys


def main():
    print(convert(str(input("Hours: ")).rstrip()))


def convert(s):
    matches = re.search(r"^(\d{1,2})(:\d{2})?\s{1}(AM|PM)\s{1}to\s{1}(\d{1,2})(:\d{2})?\s{1}(AM|PM)$", s)
    if matches:
        d1,d2,d3,d4,d5,d6 = matches.groups()
        d1 = int(d1)
        d4 = int(d4)
        #Check Format {1} or {2} or invalid format
        if d2 == None and d5 == None:
            #Format {1}
            if (0 <= d1 <= 12) and (0 <= d4 <= 12):
                #Convert to 24hour time
                d1 = check_twelve(d1,d3)
                d4 = check_twelve(d4,d6)
                return f"{d1:02d}:00 to {d4:02d}:00"
            else:
                raise ValueError("Invalid Time")
        elif d2 != None and d5 != None:
            #Format {2}
            if ((0 <= d1 <= 12) and (0 <= d4 <= 12) and
                (0 <= int(d2[1:]) <= 59) and (0 <= int(d5[1:]) <= 59)):
                #Convert to 24hour time
                d1 = check_twelve(d1,d3)
                d4 = check_twelve(d4,d6)
                return f"{d1:02d}{d2} to {d4:02d}{d5}"
            else:
                raise ValueError("Invalid Time")
        else:
            raise ValueError("Invalid Format")
    else:
        raise ValueError("Invalid Format")

def check_twelve(num, time):
    if time == "PM":
        if num == 12:
            return num
        return num + 12
    else:
        if num == 12:
            return 0
        return num
        

if __name__ == "__main__":
    main()