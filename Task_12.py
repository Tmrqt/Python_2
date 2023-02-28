s, p = map(int, input().split())
counter = 0
for x in range(s+p):
    if counter:
        break
    for y in range(s+p):
        if x+y == s and x*y == p:
            counter = 1
            print(*sorted([x, y]))