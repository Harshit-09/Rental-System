import collections
  
list1 = [10, 20, 30, 40, 50, 60]
list2 = [10, 20, 30, 50]
  
  
if collections.Counter(list1) == collections.Counter(list2):
    print("The lists l1 and l2 are the same")
else:
    print("Missing values in second list:", (set(list1).difference(list2)))