import luhn

def test_checksum_len1():
    assert luhn.checksum('7') == 7

def test_checksum_len2():
    assert luhn.checksum('13') == 5

def test_checksum_len3():
    assert luhn.checksum('383') == 3

def test_checksum_len4():
    assert luhn.checksum('2827') == 3

def test_checksum_len13():
    assert luhn.checksum('4346537657597') == 9

def test_checksum_len14():
    assert luhn.checksum('27184931073326') == 1

def test_valid():
    assert luhn.verify('356938035643809')

def test_invalid():
    assert not luhn.verify('4222222222222222')
