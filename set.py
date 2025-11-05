num=["1", "2", "3", "3", "1"]
numss = {"2","3", "4", "5"}
nums = set(num)

print(numss.union(nums))
print(numss.intersection(nums))
print(numss.difference(nums))

nums.add("4")
print(nums)
nums.remove("3")
print(nums)

my_set = {1,2,3}
my_set.remove(2)
my_set.add(99)
print(my_set)
my_set.discard(9)
print(my_set)
