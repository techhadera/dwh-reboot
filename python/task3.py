def func(x):
  if x > 50 and x % 2 != 0:
    return 1
  return 0


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(func, numbers)))
