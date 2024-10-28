h1,m1 = map(int,input().split())

h2 = m2 = 0

if h1 == 0:
    h2 = 23
    if m1 >= 45:
        m2 = m1 - 45
        h2 = h1
        print(h2, m2)
    else:
        m2 = (m1 + 60) - 45
        print(h2, m2)
else:
    if m1 >= 45:
        m2 = m1 - 45
        h2 = h1
        print(h2, m2)
    else:
        m2 = (m1 + 60) - 45
        h2 = h1 - 1
        print(h2, m2)