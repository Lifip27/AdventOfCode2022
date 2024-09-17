def split_list(input_list):
    result = []
    sublist = []
    
    for item in input_list:
        if item == "":  # If an empty string is encountered, start a new sublist
            if sublist:  # Append the current sublist to result if it's not empty
                result.append(sublist)
            sublist = []  # Reset sublist
        else:
            sublist.append(item)
    
    if sublist:  # Add the last sublist if it's not empty
        result.append(sublist)
    
    return result

def getScore(A, B):
    score = 0
    if A == "X":
        score += 1
        if B == 'A':
            score += 3
        elif B == "B":
            score += 0
        elif B == "C":
            score += 6
    elif A == "Y":
        score += 2
        if B == "A":
            score += 6
        elif B == "B":
            score += 3
        elif B == "C":
            score += 0
    elif A == "Z":
        score += 3
        if B == "A":
            score += 0
        elif B == "B":
            score += 6
        elif B == "C":
            score += 3

    return score

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    rounds = split_list(data)[0]
    print(rounds)
    Points = 0
    for i in rounds:
        opps,choice = i.split()
        Points += getScore(choice, opps)

print(Points)
    
