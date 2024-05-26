dict = {}
with open("poem.txt","r") as f:
    for line in f:
        for i in line.split():
            i = i.replace( '\n', '')
            if not i in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        # tokens = line.split(',')
        # try:
        #     temperature = int(tokens[1])
        #     dict[ tokens[0] ] = int(tokens[1])
        # except:
        #     print("Invalid temperature.Ignore the row")

print(dict)