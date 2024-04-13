months = {"January": 1,"February": 2, "March": 3,
          "April": 4, "May": 5, "June": 6,
          "July": 7, "August": 8, "September": 9,
          "October": 10, "November": 11, "December": 12}

def main():
    x = get_date()
    convert_date(x)


def get_date():
    while True:
        x = str(input("Date: ")).strip().title()
        #Format: MM/DD/YYYY
        if '/' in x:
            x = x.split('/')
            #Check for digits
            if (x[0].isdigit() == False) or (x[1].isdigit() == False) or (x[2].isdigit() == False):
                continue
            #Months check
            elif int(x[0]) > 12 or int(x[0]) < 1:
                continue
            #Days Check
            elif int(x[1]) > 31 or int(x[1]) < 1:
                continue
            #Year Check
            elif len(x[2]) != 4:
                continue
            else:
                return x
        #Format: Month DD, YYYY
        elif ',' in x:
            x = x.split()
            #Check for digits
            if (x[1][:-1].isdigit() == False) or (x[2].isdigit() == False):
                continue
            #Month Check
            elif x[0] not in months.keys():
                continue
            #Day Check (Format: 'DD,')
            elif int(x[1][:-1]) > 31 or int(x[1][:-1]) < 1:
                continue
            #Year Check
            elif len(x[2]) != 4:
                continue
            else:
                return x
        else:
            continue


def convert_date(date):
    #Check which of the two formats is the inputted one
    if date[0] in months.keys():
        #From Month DD, YYYY ------> YYYY-MM-DD
        print(f"{date[2]}-{int(months[date[0]]):02d}-{int(date[1][0]):02d}")
    else:
        #From MM/DD/YYYY ------> YYYY-MM-DD
        print(f"{date[2]}-{int(date[0]):02d}-{int(date[1][0]):02d}")


main()
