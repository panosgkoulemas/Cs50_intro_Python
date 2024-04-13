#Count the number of times the word 'um' is in the input string
import re
import sys


def main():
    print(count(str(input("Text: ")).rstrip()))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()