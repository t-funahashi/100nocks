g = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
g = g.split()
g_dict = dict()
for i,t in enumerate(g):
    if i+1 in (1,5,6,7,8,9,15,16,19):
        g_dict.setdefault(t[0],t)
    else:
        g_dict.setdefault(t[:2],t)
else:
    print(g_dict)
