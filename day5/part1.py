with open("input.txt", "r") as file:
    lines = file.readlines()
    coloane = [line.replace('\n', "") for line in lines if "move" not in line][:-2]
    mutari = [line.replace('\n', "") for line in lines if "move" in line]
    #  print(coloane)
    # print(mutari)
    numere_coloane = max(len(line.split()) for line in coloane)
    realcolumns = [[] for i in range(numere_coloane)]
    coloane = list(reversed(coloane))
    for line in coloane:
        for i in range(numere_coloane):
              pos = i * 4 + 1
              if line[pos] != ' ' and len(line) > pos : 
                   realcolumns[i].append(line[pos])
                
    print(realcolumns)
    for move in mutari:
        num = int(move.split()[1])
        loc = int(move.split()[3])-1
        dest = int(move.split()[5])-1
        realcolumns[dest] += realcolumns[loc][-num:]
        realcolumns[loc] = realcolumns[loc][:-num]
        print(realcolumns)
        # print(num,loc,dest)
        # print(move)
    
    toplayer = ""
    for i in realcolumns:
         toplayer += i[-1]
    print(toplayer)
    # print(coloane)
    # print(empty_list)
    # print(numere_coloane)