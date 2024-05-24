def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) <= 6 and len(plate) >= 2 and plate[0:2].isalpha() and plate.isalnum():
        for i in plate:
            if i.isdigit():
                result = plate.index(i)
                if plate[result:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        return True

main()
