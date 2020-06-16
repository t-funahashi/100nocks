import gzip
import os
import re
import json

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
                        Text = text_obj['text']
                        break

            # What is categories?
            Text = Text.split('\n')
            for t in Text:
                if ' = ' in t:
                    print(t)
