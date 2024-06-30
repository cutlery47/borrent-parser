from typing import Union

class Encoder:

    def encode(self, data: Union[str, int, dict, list]) -> bytes:
        if isinstance(data, str):
            return self._encode_str(data)
        elif isinstance(data, int):
            return self._encode_int(data)
        elif isinstance(data, dict):
            return self._encode_dict(data)
        else:
            return self._encode_list(data)

    @staticmethod
    def _encode_str(str_: str) -> bytes:
        length = str(len(str_))
        return length.encode() + b":" + str_.encode()

    @staticmethod
    def _encode_int(int_: int) -> bytes:
        return b"i" + str(int_).encode() + b"e"

    def _encode_dict(self, dict_: dict) -> bytes:
        res = b"d"
        for key in dict_.keys():
            res += self.encode(key)
            res += self.encode(dict_[key])
        res += b"e"

        return res

    def _encode_list(self, list_: list) -> bytes:
        res = b"l"
        for el in list_:
            res += self.encode(el)
        res += b"e"

        return res
