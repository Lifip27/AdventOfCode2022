def valoare(letter:str):
    micL = 96
    mareL = 38
    if letter.islower():
        return ord(letter)-micL  
    else:
        return ord(letter)-mareL
    


with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip().replace("\n", '')
        fh = set(line[:len(line)//2])
        sh = set(line[len(line)//2:])
        common = list(fh.intersection(sh))[0]
        print(common)    
        value = valoare(common)
        sum += value
    print(sum)
    


