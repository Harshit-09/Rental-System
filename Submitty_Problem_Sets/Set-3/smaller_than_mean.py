n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))
k = avg
print ("The list : " + str(a))

count = 0
for j in a :
    if j > k :
        count = count + 1
print ("The numbers greater than 4 : " + str(count))