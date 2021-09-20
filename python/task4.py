dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dict = {}

for key, val in dict.items():
  if val >= 3:
    new_dict[key] = val

print(new_dict)