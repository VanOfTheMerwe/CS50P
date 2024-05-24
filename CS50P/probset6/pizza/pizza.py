import sys
import csv
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) == 2:
            pizza = check_file(sys.argv[1])
            tabel = tabulate_file(pizza)
            print(tabulate(tabel, headers="keys", tablefmt="grid"))
        elif len(sys.argv) >= 3:
            sys.exit('Too many command-line arguments')
        elif len(sys.argv) <= 1:
            sys.exit('Too few command-line arguments')
    except FileNotFoundError:
        sys.exit('File not found')

# check and open the csv file
def check_file(file):
    check = file.split('.')
    if check[1] != "csv":
        sys.exit('Not a csv file')


# tabulate the csv file
def tabulate_file(menu):
    menu = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
    return menu


if __name__ == "__main__":
    main()

