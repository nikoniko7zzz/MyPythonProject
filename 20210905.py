s = 0
n = 1
while n <= 10:
    s += n
    print(s)
    n += 1
print('end')

l = [2, 3, 5, 7, 11]
i = 0
while i < len(l):
    if l[i] == 3:
        print('found')
        break
    i += 1

pets = ['dog', 'cat', 'bird']
for p in pets:
    print(p)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:     # (1)
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]: # (2)
        print(i * j, end='\t')            # (3)
    print()