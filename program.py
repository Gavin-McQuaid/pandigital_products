def contains_all_characters(string):
	characters = ['1','2','3','4','5','6','7','8','9']
	for c in characters:
		if string.count(c) != 1:
			return False
	return True
nums = []
i = 1
while len(str(i)) <= 4:
	j = 1
	while len(str(i)) + len(str(j)) + len(str(i*j)) <= 9:
		s = str(i) + str(j) + str(i*j)
		if contains_all_characters(s) and len(s) == 9 and i * j not in nums:
			nums.append(i * j)
			
		j += 1

	

	i += 1

print(sum(nums))
