from src import Encoder
import pytest

@pytest.fixture
def encoder():
    return Encoder()

def test_string(encoder):
    string_1 = "spam"
    string_2 = ""

    enc_string_1 = encoder.encode(string_1)
    enc_string_2 = encoder.encode(string_2)

    assert enc_string_1 == b"4:spam"
    assert enc_string_2 == b"0:"

def test_int(encoder):
    num_1 = 45
    num_2 = 0

    enc_num_1 = encoder.encode(num_1)
    enc_num_2 = encoder.encode(num_2)

    assert enc_num_1 == b"i45e"
    assert enc_num_2 == b"i0e"

def test_list(encoder):
    list_1 = ["spam", "eggs"]
    list_2 = []

    enc_list_1 = encoder.encode(list_1)
    enc_list_2 = encoder.encode(list_2)

    assert enc_list_1 == b"l4:spam4:eggse"
    assert enc_list_2 == b"le"

def test_dict(encoder):
    dict_1 = {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"}
    dict_2 = {}

    enc_dict_1 = encoder.encode(dict_1)
    enc_dict_2 = encoder.encode(dict_2)

    assert enc_dict_1 == b"d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee"
    assert enc_dict_2 == b"de"

