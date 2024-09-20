with open("input.txt", 'r') as f:
    data = f.read().strip().split("\n")
    words = [ch for ch in data]
    for word in data:
        lista = list(word)
        listw = []
        for letter in word:
            listw.append(letter)
            if len(listw) > 3:
                last = listw[-4:]
                if len(last) == len(set(last)):
                    result = word.find("".join(last)) + 4
                    print(result)
                    break

                    
