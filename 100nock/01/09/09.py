t = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

def sort_rand(text):
    import random
    char = ''
    t = text.split()
    for a in t:
        l = list(a[1:-1])
        if len(l) > 2:
            random.shuffle(l)
            l.insert(0,a[0])
            l.insert(len(l),a[-1])
            char = char + ''.join(l) + ' '
        else:
            char += f'{a} '
    return char
print(sort_rand(t))
