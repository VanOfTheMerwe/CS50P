def main():
    amount = getInt()
    print(f"{amount}")

def getInt():
    while True:
        try:
            va = input("a: ").split("/")
            vc = float((int(va[0])/int(va[1]))*100)
            if int(va[0]) <= int(va[1]):
                if vc >= 99:
                    print("F")
                elif vc <= 1:
                    print("E")
                else:
                    print(f"{round(float(vc))}%")
                exit()
            else:
                return getInt()
        except (ValueError, ZeroDivisionError):
            continue

main()

