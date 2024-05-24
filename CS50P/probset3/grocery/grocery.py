list = []
count = {}


while True:
    try:
        grocery = input().upper()
        list.append(grocery)
    except EOFError:
        print("")
        for i in list:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1

        for key, value in sorted(count.items()):
            print(value,key)
        exit()
