import sys

def main():
    # print(sys.argv[1])
    if len(sys.argv) == 2:
        name = is_valid(sys.argv[1])
        print(count_lines(name))
    elif len(sys.argv) >= 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) <= 1:
        sys.exit('Too little command-line arguments')



# check if the sys argument is valid
def is_valid(name):
    check = name.split('.')
    if check[-1] != "py":
        sys.exit('Not a Python file')

# check if there are lines and how many in the code
def count_lines(lines):
    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        linecount = 0

        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                continue
            elif len(line) == 0:
                continue
            else:
                linecount += 1
        return linecount
    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == "__main__":
    main()



