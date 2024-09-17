def valoare(letter:str):
    micL = 96
    mareL = 38
    if letter.islower():
        return ord(letter)-micL
    else:
        return ord(letter)-mareL
    


with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.replace("\n", '') for line in lines]
    print(lines)
    n = 3
    x = [lines[i:i+n] for i in range(0, len(lines), n)]
    print(x)
    sum = 0
    for line in x:
        f = set(line[0])
        s = set(line[1])
        t = set(line[2])
        finter = f.intersection(s)
        sinter = list(t.intersection(finter))[0]
        value = valoare(sinter)
        sum += value
        print(sum)
        

    