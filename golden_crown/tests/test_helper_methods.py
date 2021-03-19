import pytest
from src.helper_methods import encrypt, is_ally
from src.exceptions import InvalidEncryption

@pytest.mark.parametrize("input_char, ckey, expected_char", [
    ("O", 3, "R"),
    ('W', 3, 'Z'),
    ('L', 3, 'O'),
    ('M', 7, 'T'),
    ('A', 7, 'H'),
    ('O', 7, 'V'),
    ('T', 7, 'A'),
])
def test_encrypt_positive(input_char, ckey, expected_char):

	assert encrypt(input_char, ckey) == expected_char

@pytest.mark.parametrize("input_char, ckey", [
    ("1", 3),
    (' ', 3),
    ('%', 3),
    ('^', 7),
    ('*', 7),
    ('-', 7),
    (';', 7,),
])
def test_encrypt_exception(input_char, ckey):

	with pytest.raises(InvalidEncryption) as e:
		assert encrypt(input_char, ckey)
	assert str(e.value) == "Seaser Cipher is valid only for characters in the English Alphabet.\
 {} is not part of the English Alphabet.".format(input_char)


@pytest.mark.parametrize("desired_str, msg, expected_result", [
    ("FISFU", "FDIXXSOKKOFBBMU", True),
    ("TTTHVOA", "MOMAMVTMTMHTM", True),
    ("ABCDE", "MOMAMVTMTMHTM", False),
    ("MMM", "MOMAMVTMTMHTM", True),
    ("MMMMMMM", "MOMAMVTMTMHTM", False),
    ('  GNIMOC', "SUMMER IS COMING", True),
    ('  ', "SUMMER IS COMING", True),
    ('   ', "SUMMER IS COMING", False),
])
def test_is_ally(desired_str, msg, expected_result):

    assert is_ally(desired_str, msg) == expected_result