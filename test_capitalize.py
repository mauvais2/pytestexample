import cap_string as cap

def test_capitalize_string():
    assert cap.capitalize_string('test') == 'Test'
    
def test_capitalize_string_fail():
    assert cap.capitalize_string('test') != 'test'

def test_capitalize_atom_string():
    assert cap.capitalize_string('atom') == 'Atom'
