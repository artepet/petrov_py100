list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

lst1 = []
count = 0

for i in list_:
	if i not in lst1:
		count = count + 1
		lst1.append(i)

print(sum(lst1))
print(count)
print(float(round(sum(lst1) / len(lst1), 5)))