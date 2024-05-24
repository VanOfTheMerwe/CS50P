from validator_collection import checkers

def main():
    print(check_email(input('email: ')))

def check_email(epos):
    if checkers.is_email(epos):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__":
    main()
