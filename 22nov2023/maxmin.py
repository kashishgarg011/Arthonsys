#11. Find the maximum and minimum values in a list of numbers.
numbers = [5, 8, 2, 10, 15, 3]
for num in numbers:

    for j in numbers:

        if j>num:
            max_value=j
        if j<num:
            min_value=j

print("Maximum value:", max_value)
print("Minimum value:", min_value)