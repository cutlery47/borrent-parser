from src.decoder import Decoder
import pytest

@pytest.fixture
def decoder():
    return Decoder()

def test_string(decoder):
    string_1 = b"4:spam"
    string_2 = b""

    dec_string_1 = decoder.decode(string_1)
    dec_string_2 = decoder.decode(string_2)

    assert dec_string_1 == "spam"
    assert dec_string_2 == ""

def test_int(decoder):
    num = b"i45e"
    dec_num = decoder.decode(num)
    assert dec_num == 45

def test_list(decoder):
    list_1 = b"l4:spam4:eggse"
    list_2 = b"le"

    dec_list_1 = decoder.decode(list_1)
    dec_list_2 = decoder.decode(list_2)

    assert dec_list_1 == ["spam", "eggs"]
    assert dec_list_2 == []

def test_dict(decoder):
    dict_1 = b"d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee"
    dict_2 = b"de"

    dec_dict_1 = decoder.decode(dict_1)
    dec_dict_2 = decoder.decode(dict_2)

    assert dec_dict_1 == {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"}
    assert dec_dict_2 == {}
