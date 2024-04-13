def convert(txt: str):
    if ':)' in txt:
        txt = txt.replace(":)","🙂")
    if ':(' in txt:
        txt = txt.replace(":(","🙁")
    return txt

def main():
    x = str(input("Enter: "))
    x = convert(x)
    print(x)

main()
