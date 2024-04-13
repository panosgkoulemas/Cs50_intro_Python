x = str(input("camelCase: "))

words = []
while True:
    count = 0
    for i in range(len(x)):
        if x[i].isupper():
            if i == 0:
                continue
            words.append(x[:i].lower())
            x = x[i:]
            count = count + 1
            break
    if count == 0:
        break
words.append(x.lower())
print('_'.join(words))