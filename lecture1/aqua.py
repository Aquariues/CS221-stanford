"""
	count the diffent between 2 string a,b
"""
def countDiff(a,b):
	temp_a = []
	temp_b = []
	count = 0
	for i in range(len(a)):
		if a[i] not in temp_a:
			temp_a.append(a[i])

	for i in range(len(b)):
		if b[i]not in temp_b:
			temp_b.append(b[i])

	if len(temp_b) > len(temp_a):
		temp = temp_a
		temp_a = temp_b 
		temp_b = temp

	print(temp_a)
	print(temp_b)

	for i in range(len(temp_a)):
		if temp_a[i] not in temp_b:
			print(temp_a[i])
			count = count + 1
	return count

print(countDiff('a cat!','the cats!'))