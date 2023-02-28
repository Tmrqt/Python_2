n = int(input())
counter = 0
for i in range(n):
    coin = int(input())
    if coin == 1:
        counter += 1
if counter < n/2:
    print (counter)
else:
    print (n-counter)