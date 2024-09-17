with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.replace("\n", '') for line in lines]
    pairs = []
    repetari = 0
    for line in lines:
        x = line.split(",")
        primu, aldoilea = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        if primu[0] != aldoilea[0]:
            if primu[0] > aldoilea[0]:
                inauntru, inafara = primu, aldoilea
            else:
                inauntru, inafara = aldoilea, primu
        else:
            if primu[1] < aldoilea[1]:
                inauntru, inafara = primu, aldoilea
            else:
                inauntru, inafara = aldoilea, primu
        if  inauntru[1] <= inafara[1]:
            repetari += 1
        print(inauntru)
        print(inafara)
    print(repetari)
