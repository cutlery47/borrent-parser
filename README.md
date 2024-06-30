# borrent-parser
A bit-torrent protocol file parser.

Can be installed using:

    pip install borrent-parser

The module provides Encoder and Decoder classes, which are capable of parsing any bencoded file.

# Example
    
    dec = Decoder()
    dec.decode(b"d4:spaml2:ab3cdeee")
    # expected output: {"spam": ["ab", "cde"]}

    enc = Encoder()
    enc.encode([["abc", "def"], {"a": 123}])
    # expected output: b"ll3:abc3:defed1:ai123eee"

For more info on bencode, feel free to check out: https://en.wikipedia.org/wiki/Bencode
    
