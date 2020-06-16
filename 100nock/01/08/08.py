import re

t = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

def cipher(text):
    char = ''
    m = re.compile(r'[a-z]',re.A)
    for t in text:
        r = m.fullmatch(t)
        if r is not None:
            a = 219 - ord(t)
            tt = chr(a)
        else:
            tt = t
        char += tt
    return(char)

print(cipher(t))