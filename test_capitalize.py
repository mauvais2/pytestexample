import cap_string as cap

def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def test_capitalize_string():
    assert cap.capitalize_string('test') == 'Test'
    
def test_capitalize_string_fail():
    assert cap.capitalize_string('test') != 'test'
