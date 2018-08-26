list = []

for i in range(1, 44):
	list.append(i)

for i in list:
	print(i)


pageUnit = 10
pageSize = 10

pageIndex = 1
start = (pageIndex-1) * pageUnit
end = start + pageUnit
print(list[start:end])

pageIndex = 2
print(list[10:20])

pageIndex = 3
print(list[20:30])

pageIndex = 4
print(list[30:40])

pageIndex = 5
print(list[40:50])
