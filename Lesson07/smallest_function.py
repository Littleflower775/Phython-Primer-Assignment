def find_smallest(numbers):
	# set smallest variable to be equal to the first value
	smallest = numbers[0]

	# for every number in the list of numbers
	for number in numbers:
		# check whether the current number is smaller than the current smallest
		if number < smallest:
			# if it is smaller, set the current smallest to the current number
			smallest = number

	return smallest

my_list = [5, 10, 3, 6, 7, 14]
second_list = [-1, -4, -5, -2, -3]

smallest_in_list = find_smallest(my_list)
print(smallest_in_list)

smallest_in_list = find_smallest(second_list)
print(smallest_in_list)