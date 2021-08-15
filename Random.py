from random import randint

random_list = []
output_list = []

for x in range(20):
	random_list.append(randint(0,20))
print(random_list)

# convert to odd numbers
for i in random_list:
	if i%2 == 0:
		i += 1
		output_list.append(i)
		continue
	output_list.append(i)
print(output_list)