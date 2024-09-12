'''This is the tests for each of the functions'''
from CS50P.project.project import convert_a, convert_e, convert_o, convert_i, convert_u, convert_h, convert_b, convert_g, convert_char_to_num, add_special, set_case
import random

def main():
    test_conversion()
    test_special()
    test_cases()

def test_conversion():
    '''This tests the outcome of the conversion between letters and numbers.'''
    assert convert_a('a') == '4'
    assert convert_b('b') == '8'
    assert convert_e('e') == '3'
    assert convert_o('o') == '0'
    assert convert_i('i') == '1'
    assert convert_u('u') == 'v'
    assert convert_h('h') == '#'
    assert convert_g('g') == '9'
    assert convert_char_to_num('i like beans') == '1 l1k3 834ns'

def test_cases():
    '''This tests the outcome of the manipulation of the cases.'''
    assert set_case('i like beans') == 'i liKE BEANS'
    assert set_case('abcdefghijklmnop') == 'abcdEFGHIJKLMNOP'

def test_special():
    '''This tests whether or not the end phrase contains a special character.'''
    phrase = 'password'
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '~', '`']
    random.seed(42)  # Set a seed to make the test reproducible.
    result = add_special(phrase)
    assert len(result) == len(phrase) + 1 # Check that the result is the original phrase plus one special character.
    assert result[-1] in special_characters
    results = {add_special(phrase) for _ in range(100)} # Call the function multiple times to check for randomness.
    assert len(results) > 1 # Ensure we have a variety of different results.
    '''I acquired help with the figuring out how to test the random stuff.
    Thank you.'''
    # assert add_special('i like beans')[specials.__len__()] in specials
    # print('test_specials passed')
    '''The above does not work but is also code retrieved for assistance of testing the random stuff.'''
