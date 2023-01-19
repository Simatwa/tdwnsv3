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
from random import sample

all_chars = []


class verifiers:
    def __init__(self, request: object, config: dict):
        self.request = request
        self.config = config

    def redirect_home(self):
        return f"""
		<!DOCTYPE html><html>
		<head>
		   <script type='text/javascript' src='/{self.config['hidden_dir']}/js'></script>
		  </head>
		 <body style='background-color:red;' onload="ajhsvysbjuhajannqyafeeusbbeg()">
		 </body></html>"""


class __smart_sec:
    def __init__(
        self,
        level: int,
    ):
        self.sec_level = {
            1: 10,
            2: 20,
            3: 30,
            4: 50,
            5: 80,
            6: 120,
            7: 170,
            8: 230,
            9: 300,
            10: 400,
        }
        self.level = self.sec_level[level]
        self.mod_chars()
        if self.level > 4:
            all_chars.extend(all_chars * level)

    # Adds the chat to the list
    def mod_chars(self):
        ts = [[65, 91], [97, 122]]
        for chrs in ts:
            for x in range(chrs[0], chrs[1]):
                all_chars.append(chr(x))

    # Defines the home routing
    def set_home_folder(self):
        return "".join(sample(all_chars, self.level))

    def set_static_folder(self):
        return "".join(sample(all_chars, int(self.level / 2)))


def new_cookie(size=24):
    size = len(all_chars) - 1 if size > len(all_chars) else size
    return "".join(sample(all_chars, size))


def credentials(level: int):
    __secure = __smart_sec(level)
    static = __secure.set_static_folder()
    home = __secure.set_home_folder()
    upload = static + home[::-1]
    return {
        "home": home,
        "static": static,
        "upload": upload,
        "data_name": new_cookie(24),
        "folder_name": new_cookie(22),
        "hidden_dir": new_cookie(52),
        "first": new_cookie(8),
    }
