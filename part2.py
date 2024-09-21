with open("input.txt", 'r') as data:
    current_path = ''
    directories = {'/home': 0}
    for line in data.read().splitlines():
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == '..':
                    current_path = current_path[:current_path.rindex('/')]
                elif line[2] == '/':
                    current_path = '/home'
                else:
                    current_path = current_path + "/" + line[2]
                    directories[current_path] = 0
        else:
            if line[0] != 'dir':
                temp_path = current_path
                while temp_path != '':
                    directories[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex('/')]

    free_space = directories["/home"] - (70000000 - 30000000)
    celmaimicdirect = directories['/home']
    for _, directory in directories.items():
        if free_space < directory < celmaimicdirect:
            celmaimicdirect = directory
    print(celmaimicdirect)
