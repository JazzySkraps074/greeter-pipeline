from greeter import greet

def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"

def test_greet_with_empty_string():
    assert greet("") == "Hello, stranger!"

def test_greet_with_none():
    assert greet(None) == "Hello, stranger!"
