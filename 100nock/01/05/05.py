t = 'I am an NLPer'
t = t.split()
c = ''.join(t)

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

ret = craete_n_gram(t)
print(ret)


