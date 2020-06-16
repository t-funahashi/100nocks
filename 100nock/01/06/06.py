t1 = 'paraparaparadise'
t2 = 'paragraph'

def craete_n_gram(seq,N=2):
    if isinstance(seq,list):
        try:
            char = ' '.join(seq)
        except:
            return False
        word = char.split()
        char = ''.join(word)
    elif isinstance(seq,str):
        word = seq.split()
        char = ''.join(word)
    else:
        return False

    char_N_gram = [ char[i:i+N] for i in range(len(char)-(N-1))]
    word_N_gram = [ [ word[i+j] for j in range(N)] for i in range(len(word)-(N-1))]
    return char_N_gram,word_N_gram

X = set(craete_n_gram(t1)[0])
Y = set(craete_n_gram(t2)[0])

wa = X | Y
seki = X & Y
sa = X - Y

print('X',X)
print('Y',Y)
print('和集合',wa)
print('積集合',seki)
print('差集合',sa)
if 'se' in X:
    print('"se" in X')
else:
    print('"se" not in X')
if 'se' in Y:
    print('"se" in Y')
else:
    print('"se" not in Y')
