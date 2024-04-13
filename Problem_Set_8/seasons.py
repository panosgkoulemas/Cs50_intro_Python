from datetime import date
import sys
import re
import inflect

def main():
    print(convert(str(input("Date of Birth: ")).rstrip()))

def convert(s):
    #Accepted Format: YYYY-MM-DD
    matches = re.search(r"^\d{4}-\d{2}-\d{2}$", s)
    if matches:
        s = s.split('-')
        birth_date = date(int(s[0]), int(s[1]), int(s[2]))
        today = date.today()
        p = inflect.engine()
        return f"{p.number_to_words(((today - birth_date).days - 1) * 24 * 60).capitalize().replace('and ', '')} minutes"
    else:
        sys.exit("Invalid Format: YYYY-MM-DD")


if __name__ == "__main__":
    main()