def f(s: str):
    la = lb = lc = -1
    count = 0

    for idx, c in enumerate(s):
        if c == "a":
            la = idx
        elif c == "b":
            lb = idx
        else:
            lc = idx
        m = min(la, lb, lc)
        if m != -1:
            print(m, c, lc)
            x = m + 1
            count += x
    return count


s = "abc"
print(f(s))
