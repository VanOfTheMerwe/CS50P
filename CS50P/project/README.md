# Password Generator
## The CS50P Final project
### Video Demo: https://youtu.be/2UkXwqNRoaw
## Description:
A Password Generator created by Drikus van der Merwe on the 24th of June 2024.

The libraries that I have imported are time, random and the sys library.
I used the sleep function from the time library to give the program a more organic flow. I didn't want it to feel rushed.
I used the random library for my add_special function.
I used the sys library to quit the program once it has been completed.

## Functions:
### convert_char_to_num:
This function converts some of the alphanumerical characters in the user's input into numbers that are representative or similiar to that character.
The a is converted into a 4.
The e is converted into a 3.
The o is converted into a 0.
The i is converted into a 1.
The u is converted into a v.
The h is converted into a #.
The b is converted into an 8.
The g is converted into a 9.
I wanted to do the numbers to characters as well but that was a little more difficult.

### set_case:
This function sets the case for the string and makes sure that not all of the input is lowercase nor uppercase but a mix of both.
The first four characters if they are part of the alphabet are converted to lowercase and the other following characters are converted to uppercase if they are in fact alphabet characters.

### add_special:
This function adds a random special character at the end of the string. This was where I used the random library. The random then chooses a character from a list that I created and then adds from that list to the end and then returns it as a whole.

I recall main on line 17 in the event that the user does not enter a string with the length of 12 characters.

My GitHub username is VanOfTheMerwe
My EdX username is Drikus_Van_Der_Merwe

