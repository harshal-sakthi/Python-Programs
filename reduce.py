from functools import reduce

"""nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce (lambda x, y: x + y, nums)
print(total)"""

"""numsi = [7, 22, 50, 10]
maxi = reduce(lambda x,y : x if x > y else y, numsi)
print(maxi)"""

numsii = [7, 22, 50, 10]
maxi = max(numsii)
print(maxi)