from datetime import datetime, timedelta, date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        birthday = input("What is your birthday? ")
        dae = date_math(birthday)
    # print(dae)
        minutes = convert_minutes(dae)
    # print(minutes)
        regte = p.number_to_words(minutes, andword='').capitalize()
        print(regte, "minutes")
    except ValueError:
        sys.exit('Invalid Date')

def date_math(verjaarsdag, today = None):
    today = date.today()
    # today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    dateformat = "%Y-%m-%d"
    verjaar = datetime.strptime(verjaarsdag, dateformat).date()
    # verjaar = verjaar.replace(hour=0, minute=0, second=0, microsecond=0)
    datum = today - verjaar
    # print(datum)
    return datum

def convert_minutes(dae):
    minute = dae.total_seconds() / 60
    return round(minute)

if __name__ == "__main__":
    main()

