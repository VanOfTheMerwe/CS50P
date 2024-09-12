from time import sleep
import random
import sys

def main():
    print('Hello and welcome to the password generator, this will generate a password for you in no time and hopefully be one you can remember.')
    sleep(2)
    print('Please provide a phrase that you will remember. ')
    user_input = str(input('The phrase: ')).strip(' ').lower()
    if len(user_input) >= 12:
        new = convert_char_to_num(user_input)
        new = set_case(new)
        new = add_special(new)
        print(new)
        sys.exit('If the system does not allow spaces inbetween characters, just remove it.')
    else:
        main()
    '''We run main again and again until the user gives us the correct response of 12 characters in length'''

def convert_char_to_num(phrase):
    '''Converts the characters given into numerical values.'''
    phrase = convert_a(phrase)
    phrase = convert_b(phrase)
    phrase = convert_e(phrase)
    phrase = convert_o(phrase)
    phrase = convert_i(phrase)
    phrase = convert_u(phrase)
    phrase = convert_h(phrase)
    phrase = convert_g(phrase)
    return phrase
    # I know the multiple functions created to do this was unneccesary but it works so I am not changing jack shit.

def convert_a(phrase):
    if 'a' in phrase:
        return phrase.replace('a','4') #This just converts a to 4.
    else:
        return phrase

def convert_e(phrase):
    if 'e' in phrase:
        return phrase.replace('e','3') #This just converts e to 3.
    else:
        return phrase

def convert_o(phrase):
    if 'o' in phrase:
        return phrase.replace('o','0') #This just converts o to 0.
    else:
        return phrase

def convert_i(phrase):
    if 'i' in phrase:
        return phrase.replace('i','1') #This just converts i to 1.
    else:
        return phrase

def convert_u(phrase):
    if 'u' in phrase:
        return phrase.replace('u','v') #This converts u to v.
    else:
        return phrase

def convert_h(phrase):
    if 'h' in phrase:
        return phrase.replace('h','#')
    else:
        return phrase

def convert_b(phrase):
    if 'b' in phrase:
        return phrase.replace('b','8')
    else:
        return phrase

def convert_g(phrase):
    if 'g' in phrase:
        return phrase.replace('g','9')
    else:
        return phrase

def add_special(phrase):
    '''Adds the special characters to the string such as required for a decent password.'''
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '~', '`']
    phrase = phrase + random.choice(specials)
    return phrase

def set_case(phrase):
    '''Converts all the cases to what I want them to be.'''
    return phrase[0:4].lower() + phrase[4:].upper()

if __name__ == "__main__":
    main()

'''VanOfTheMerwe on 24th of June 2024'''
