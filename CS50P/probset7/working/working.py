import re
import sys

def main():
    print(convert(input('Hours: ')))

def convert(tyd):
    try:
        if hours := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$",tyd):
            if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
                raise ValueError
            eerste = maak(int(hours.group(1)), hours.group(2), hours.group(3))
            tweede = maak(int(hours.group(4)), hours.group(5), hours.group(6))
            return eerste + " to " + tweede
        else:
            raise ValueError
    except ValueError:
        sys.exit(ValueError)

def maak(ure,minute,tyd):
    try:
        if tyd == "PM":
            if ure == 12:
                ure = 12
            else:
                ure += 12
        else:
            if ure == 12:
                ure = 0
        if minute == None:
            minute = ':00'
            resultaat = f"{ure:02}{minute:02}"
        else:
            resultaat = f"{ure:02}:{minute:02}"

        return resultaat
    except ValueError:
        sys.exit(ValueError)


if __name__ == "__main__":
    main()
