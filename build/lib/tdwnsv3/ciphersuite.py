"""'
MIT License

Copyright (c) 2023 Simatwa Caleb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from cryptography.fernet import Fernet


class encryption:
    def __init__(self, key: bytes, args: object, config: dict):
        self.args = args
        self.config = config
        self.__fernet = Fernet(key)

    # Encrypts the data
    def encrypt(self, text: str) -> str:
        return self.__fernet.encrypt(text.encode()).decode()

    # Decrypts the data
    def decrypt(self, text: str) -> str:
        try:
            text = text.encode()
            decr = self.__fernet.decrypt(text).decode()
            rp = (True, decr)
        except Exception as e:
            rp = (False, e)
        return rp

    # Main method
    def handle_cipher(self, text, enc=False, dec=False, path=False):
        if self.args.encrypt:
            if enc:
                rp = (True, "/" + self.config["home"] + "/" + self.encrypt(path))
            else:
                rp = self.decrypt(text)
        else:
            rp = (True, text)
        return rp


if __name__ == "__main__":
    key = Fernet.generate_key()
    ciph = encryption(key)
    msg = "Hello world"
    for _ in range(4):
        enc = ciph.encrypt(msg)
        dec = ciph.decrypt(enc)
        print(enc, dec)

# 020123191601
