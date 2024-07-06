from src import Decoder
from src import Encoder
from bcoding import bencode, bdecode
from tests.testcase_generator import TestCaseGenerator
import pytest

@pytest.fixture
def generator():
    return TestCaseGenerator()

@pytest.fixture
def decoder():
    return Decoder()

@pytest.fixture
def encoder():
    return Encoder()


def test_string(decoder, encoder, generator):
    for i in range(100):
        gen_string = generator.generate_string(max_len=20)
        enc_string = encoder.encode(gen_string)
        dec_string = decoder.decode(enc_string)
        assert gen_string == dec_string

def test_int(decoder, encoder, generator):
    for i in range(100):
        gen_int = generator.generate_integer(max_int=10000)
        enc_int = encoder.encode(gen_int)
        dec_int = decoder.decode(enc_int)
        assert gen_int == dec_int

def test_list(decoder, encoder, generator):
    for i in range(100):
        try:
            gen_list = generator.generate_list(max_list_len=2, max_int=10000, max_string_len=20, max_dict_keys=2)
            enc_list = encoder.encode(gen_list)
            dec_list = decoder.decode(enc_list)
            assert gen_list == dec_list
        except RecursionError:
            pass

def test_dict(decoder, encoder, generator):
    for i in range(100):
        try:
            gen_dict = generator.generate_dict(max_list_len=2, max_int=10000, max_string_len=20, max_dict_keys=2)
            enc_dict = encoder.encode(gen_dict)
            dec_dict = decoder.decode(enc_dict)
            assert gen_dict == dec_dict
        except RecursionError:
            pass

def test_file(decoder, encoder, generator):
    with open('music.torrent', "rb") as file:
        raw = file.read()

    dec = Decoder().decode(raw)
    dec_2 = bdecode(raw)

    assert dec == dec_2
