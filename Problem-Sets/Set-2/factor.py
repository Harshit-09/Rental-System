
import math   
  
# Function to calculate sum  
# of all divisors of given 
#  natural number 
def divSum(n) : 
      
    # Final result of summation  
    # of divisors 
    result = 0
    
    # find all divisors which 
    # divides 'num' 
    for i in range(2,(int)(math.sqrt(n))+1) : 
  
        # if 'i' is divisor of 'n' 
        if (n % i == 0) : 
  
            # if both divisors are same  
            # then add it only once 
            # else add both 
            if (i == (n/i)) : 
                result = result + i 
            else : 
                result = result + (i + n//i) 
          
          
    # Add 1 and n to result as above  
    # loop considers proper divisors 
    # greater than 1. 
    return (result + n + 1) 
    
# Driver program to run the case 
n = int(input("\nenter number::"))
print("result is::",divSum(n))        