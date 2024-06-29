import random
import string
from typing import Union

class TestCaseGenerator:

    @staticmethod
    def generate_string(max_len: int) -> str:
        length = random.randint(1, max_len)
        gen_string = ""

        for i in range(length):
            letter = random.choice(string.ascii_letters)
            gen_string += letter

        return gen_string

    @staticmethod
    def generate_integer(max_int: int) -> int:
        return random.randint(-max_int, max_int)

    def generate_list(self, max_string_len,  max_int, max_list_len, max_dict_keys) -> list:
        res = []
        for i in range(max_list_len):
            el = self.generate_random(max_string_len, max_int, max_list_len, max_dict_keys)
            res.append(el)

        return res

    def generate_dict(self, max_string_len,  max_int, max_list_len, max_dict_keys) -> dict:
        res = {}
        for i in range(max_dict_keys):
            key = self.generate_random(max_string_len, max_int, max_list_len, max_dict_keys, is_dict_key=True)
            value = self.generate_random(max_string_len, max_int, max_list_len, max_dict_keys)
            res[key] = value

        return res

    def generate_random(self, max_string_len, max_int, max_list_len, max_dict_keys,
                        is_dict_key=False) -> Union[str, int, list, dict]:

        if not is_dict_key:
            rand = random.randint(1, 4)
        else:
            rand = random.randint(1, 2)

        if rand == 1:
            return self.generate_integer(max_int)
        elif rand == 2:
            return self.generate_string(max_string_len)
        elif rand == 3:
            return self.generate_list(max_string_len, max_int, max_list_len, max_dict_keys)
        else:
            return self.generate_dict(max_string_len, max_int, max_list_len, max_dict_keys)


generator = TestCaseGenerator()
print(generator.generate_dict(10, 50, 2, 2))