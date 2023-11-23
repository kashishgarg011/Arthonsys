#15. Create a dictionary from two lists (keys and values).
keys = ['Name', 'roll_No', 'Grade']
values = ['Kashish', 20, 'A']

dictionary = {keys[i]: values[i] for i in range(len(keys))}

print("Resulting dictionary:",dictionary)