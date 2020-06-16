import gzip
import os
import re
import json

from json.decoder import WHITESPACE

# ref = https://pod.hatenablog.com/entry/2017/08/31/035140
def loads_iter(s):
    size = len(s)
    decoder = json.JSONDecoder()

    end = 0
    while True:
        # Where can I find out how to use WHITESPACE?
        # https://github.com/python/cpython/blob/3.7/Lib/json/decoder.py
        # Line 132
        # Oh yeah, it was a regular expression question
        # It's convenient, but I can't use it
        idx = WHITESPACE.match(s[end:]).end()
        i = end + idx
        if i >= size:
            break
        ob, end = decoder.raw_decode(s, i)
        yield ob

if __name__ == '__main__':
    cpath = os.getcwd()
    file_path = '\\jawiki-country.json.gz'
    full_path = cpath+file_path
    if os.path.exists(full_path):
        with gzip.open(full_path,mode ='rb') as f:
            file_con = f.read().decode()
            decoder = json.JSONDecoder()

            WS = re.compile(r'[ \t\n\r]*', re.MULTILINE|re.VERBOSE|re.DOTALL)

            l = len(file_con)
            index = 0
            while True:
                add_index = WS.match(file_con[index:]).end()
                index += add_index
                if index >= l:
                    break
                text_obj ,length = decoder.raw_decode(file_con[index:])
                index += length

                for v in text_obj.values():
                    if 'イギリス' == v:
                        print(text_obj['text'])
