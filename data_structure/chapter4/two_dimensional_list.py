import pprint

a = []
print(a)

a.append([])
print(a)

a[0].append(1)
a[0].append(10)
a[0].append(100)
print(a)

a.append([])
a[1].append(2)
a[1].append(8)
a[1].append(12)
print(a)

a.append([])
a.append([])
a.append([])
a[3].append(13)
a[3].append(23)
a[3].append(33)
print(a)

print(a[1])
print(a[1][1])
print()
pprint.pprint(a)