def fact(z):  
    f = 1  
    if z == 0:  
        return f 
    else:  
        for i in range(1,z+1):  
            f = f * i  
        return f 
  
  
n=int(input("Enter the number of teams::"))  
r = int(input("how many matches should be played between each other::"))  
nCr = fact(n) / (fact(r) * fact(n - r))
print("\nNo.of combinations for n teams to play each other = %d" %(nCr))