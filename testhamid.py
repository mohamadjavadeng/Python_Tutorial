Alist = [[1,2],[2,6],[3,7],[4,6],[9,8]]
print(Alist)
A1 = []
A2 = []
for i in Alist:
    A1.append(i[0])
    A2.append(i[1])
print(A1)
print(A2)

for i in range(len(Alist)):
    globals()['list%s' % i] = Alist[i]

for i in range(len(Alist)):
    print(globals()['list%s' % i])

print(list0)