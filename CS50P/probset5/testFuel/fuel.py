def main():
    while True:
        try:
            frac = (input("Fraction: "))
            per = convert(frac)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(per))


def convert(fraction):
    f, s = fraction.split('/')
    f, s = int(f), int(s)
    if s == 0:
        raise ZeroDivisionError
    elif f > s:
        raise ValueError
    else:
        percentage = round(f / s * 100)
        return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
