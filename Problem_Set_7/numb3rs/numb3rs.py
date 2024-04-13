import re
import sys


def main():
    print(validate(str(input("IPv4 Address: "))))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.+(\d{1,3})\.+(\d{1,3})\.+(\d{1,3})$", ip)
    if matches:
        for num in matches.groups():
            if int(num) not in range(256):
                return False
        return True
    else: 
        return False
    

if __name__ == "__main__":
    main()