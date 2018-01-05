list0 = [1,2,3,4,5,6,7,8,9,10]
for i in list0:
	if i & (i-1) == 0:  # true if i is a power of 2
		print(i)

