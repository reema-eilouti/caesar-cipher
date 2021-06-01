from caesar_cipher import encrypt, decrypt, crack


def test_encrypt():
    expected ='mjqqt btwqi'
    actual= encrypt('hello world', 5)
    assert actual == expected
    print("success")
    
def test_decrypt():
    expected ='hello world'
    actual = decrypt('mjqqt btwqi', 5)
    assert actual == expected 
    print("success")

def test_crack():
    expected = 'hello world'
    actual = crack('mjqqt btwqi')
    assert actual == expected 
    print("success")


test_encrypt()
test_decrypt()
test_crack()