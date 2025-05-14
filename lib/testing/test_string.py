# lib/testing/test_string.py

def test_return_string():
    from string_functions import return_string  # Move import here, inside the test function
    assert return_string("hello") == "hello"

def test_interpolate_string():
    from string_functions import interpolate_string  # Move import here, inside the test function
    assert interpolate_string("Hello {name}", name="World") == "Hello World"
