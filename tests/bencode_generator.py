import random
import string

from src.decoder import Decoder

class BencodeGenerator:

    def generate_bencode_list(self, list_elements) -> bytes:

        res = b""
        for el in list_elements:
            res += el

        return b"l" + res + b"e"

    def generate_bencode_dict(self, max_list_len, max_string_len, max_int_len, max_dict_keys) -> bytes:
        list_elements = []
        for i in range(max_dict_keys):
            key = self.random_bencode(max_list_len, max_string_len, max_int_len, max_dict_keys)
            value = self.random_bencode(max_list_len, max_string_len, max_int_len, max_dict_keys)
            list_elements.append(key)
            list_elements.append(value)

        res = b""
        for el in list_elements:
            res += el

        return b"d" + res + b"e"

    @staticmethod
    def generate_bencode_string(max_len: int) -> bytes:
        length = random.randint(1, max_len)
        word = ""self, max_string_len,  max_int_len, max_list_len, max_dict_keys

        for i in range(length):
            letter = random.choice(string.ascii_letters)
            word += letter

        return f"{length}:{word}".encode()

    @staticmethod
    def generate_bencode_integer(max_int: int) -> bytes:
        num = random.randint(-max_int, max_int)
        return f"i{num}e".encode()

    def random_bencode(self, max_list_len, max_string_len, max_int_len, max_dict_keys):
        rand = random.randint(1, 4)
        if rand == 1:
            return self.generate_bencode_integer(max_int_len)
        elif rand == 2:
            return self.generate_bencode_string(max_string_len)
        elif rand == 3:
            return self.generate_bencode_list(max_list_len, max_string_len, max_int_len, max_dict_keys)
        else:
            return self.generate_bencode_dict(max_list_len, max_string_len, max_int_len, max_dict_keys)





