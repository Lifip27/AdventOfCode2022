with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.replace("\n", '') for line in lines]
    pairs = []
    repetari = 0
    for line in lines:
        x = line.split(",")
        primu, aldoilea = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        if primu[0] > aldoilea[0]:
            inauntru_index, inafara_index = primu, aldoilea
        else:
            inauntru_index, inafara_index = aldoilea, primu
        if inauntru_index[0] <= inafara_index[1]:
            repetari += 1
        print(repetari)


