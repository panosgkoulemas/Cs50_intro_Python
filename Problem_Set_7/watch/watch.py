import re
import sys


def main():
    print(parse(str(input("HTML: "))))


def parse(s):
    matches = re.search(r"\"https?://(www\.)?youtube\.com/embed/([a-z0-9]+)\"{1}", s, re.IGNORECASE)
    if matches:
       return f"https://youtu.be/{matches.group(2)}"
    return None


if __name__ == "__main__":
    main()
