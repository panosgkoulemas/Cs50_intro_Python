from numb3rs import validate

def test_True():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("134.1.5.254") == True

def test_False():
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("255,255.255.255") == False
    assert validate("0.1.2.1000") == False
    assert validate("256.0.1.3") == False

#run pytest test_numb3rs.py