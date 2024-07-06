from typing import Union

from io import BytesIO

# value for bytes -> int conversion
ascii_digits_start = 48

class Decoder:

    def decode(self, data) -> Union[dict, int, str, list]:
        return self._decode(data, 0)[0]

    def _decode(self, data: bytes, start: int) -> (Union[dict, int, str, list], int):
        if len(data) == 0:
            return "", 0

        if data[start] == ord('i'):
            res = self._decode_int(data, i=start+1)
        elif data[start] == ord('l'):
            res = self._decode_list(data, i=start+1)
        elif data[start] == ord('d'):
            res = self._decode_dict(data, i=start+1)
        else:
            res = self._decode_str(data, i=start)

        return res

    @staticmethod
    def _decode_int(data: bytes, i: int) -> (int, int):
        res = 0
        mult = 1

        if data[i] == ord("-"):
            mult = -1
            i += 1

        while data[i] != ord('e'):
            res = res * 10 + (data[i] - ascii_digits_start) * mult
            i += 1

        return res, i + 1

    @staticmethod
    def _decode_str(data: bytes, i: int) -> (str, int):
        strlen = 0
        while data[i] != ord(':'):
            strlen = strlen * 10 + (data[i] - ascii_digits_start)
            i += 1
        readable_data = BytesIO(data)
        readable_data.seek(i)
        res = readable_data.read(strlen)
        return res.decode(), i + strlen + 1

    def _decode_dict(self, data: bytes, i: int) -> (dict, int):
        res = {}
        while data[i] != ord('e'):
            key, i = self._decode(data, start=i)
            value, i = self._decode(data, start=i)
            res[key] = value
        return res, i + 1

    def _decode_list(self, data: bytes, i: int) -> (list, int):
        res = []
        while data[i] != ord('e'):
            el, i = self._decode(data, i)
            res.append(el)
        return res, i + 1

