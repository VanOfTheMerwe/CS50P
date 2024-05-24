from bank import value

# test the values
# test 'h' = 20
def test_h():
    assert value('hi') == 20
    assert value('hey') == 20

# test that 'hello' = 0
def test_hello():
    assert value('hello') == 0
    assert value('Hello') == 0
    
# test that other input given = 100
def test_other():
    assert value('whats up') == 100
    assert value('good afternoon') == 100

