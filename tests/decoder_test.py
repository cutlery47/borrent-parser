from bencode_generator import TestCaseGenerator

from src.decoder import Decoder
import pytest

@pytest.fixture
def decoder():
    return Decoder()

@pytest.fixture
def generator():
    return TestCaseGenerator()

def test_string(decoder, generator):
    for i in range(100):
        testcase = generator.generate_bencode_string(50)
        assert decoded == b"spam"


def test_int(decoder):
    num = b"i45e"
    decoded

