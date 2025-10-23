s = "paper"
t = "title"

if len(s) != len(t):
    print("No")
else:
    mapping = {}
    is_iso = True

    for c1, c2 in zip(s, t):
        if c1 in mapping:
            if mapping[c1] != c2:
                is_iso = False
                break
        else:
            if c2 in mapping.values():
                is_iso = False
                break
            mapping[c1] = c2

    print("Yes" if is_iso else "No")
