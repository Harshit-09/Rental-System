#importing the module
import itertools
#initializing the list
numbers = [45, 35, 138, 43, 67]
 #result
result = []
 #permutations
for permutation in itertools.permutatio(str(number) for number in numbers):
     result.append(''.join(permutation))
 #finding max
maximum = max(result, key=int)
  #printing the max
print(int(maximum))