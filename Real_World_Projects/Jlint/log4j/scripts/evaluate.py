with open("../outputs/log4j.log", 'r') as rf:
    rows = rf.readlines()
    res = 0
    for line in rows:
        idx = line.find("completed: ")
        if idx == -1:
            continue
        idx += 11
        num = ""
        while line[idx] != ' ':
            num += line[idx]
            idx += 1
        print(num)
        res += int(num)
    print("res: ", res)