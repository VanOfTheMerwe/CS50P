import inflect
# inflect is used in code when values are more than one and need to be pluralized.

namelist = []
plural = inflect.engine()

while True:
    # get the input of names and add to the list.
    try:
        name = str(input(""))
        namelist.append(name)
    # in the event of an Error skip and break to next line of code.
    except EOFError:
        print()
        break
# conjoin all the given names to the list.
greetings = plural.join(namelist)
# execute the correct output and grammar functions.

print("Adieu, adieu, to",greetings)

