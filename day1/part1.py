def split_list(input_list):
    result = []
    sublist = []
    
    for item in input_list:
        if item == "":  # If an empty string is encountered, start a new sublist
            if sublist:  # Append the current sublist to result if it's not empty
                result.append(list(map(int, sublist)))
            sublist = []  # Reset sublist
        else:
            sublist.append(item)
    
    if sublist:  # Add the last sublist if it's not empty
        result.append(list(map(int, sublist)))
    
    return result

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    top = []
    elfs = split_list(data)
    print(elfs)
    for i in elfs:
        top.append(sum(i))
    top.sort()
    print(sum(top[-1:]))
