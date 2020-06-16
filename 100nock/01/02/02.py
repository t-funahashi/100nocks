t1 = 'パトカー'
t2 = 'タクシー'
t= ''
for a,b in zip(t1,t2):
    t = t + ''.join([a,b])
else:
    print(t)
