t =  [(2, 'banana'), (3, 'apple'), (1, 'orange')]

st = lambda s : sorted(s,key = lambda s:s[1])

print(st(t))