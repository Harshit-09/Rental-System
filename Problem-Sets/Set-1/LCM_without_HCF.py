def lcm(x ,y):
    large = max(x,y)
    small = min(x,y)
    i = large
    while(True):
        if(i % small == 0):
            return i
        i = i + large

    x = 30
    y = 40
    print("LCM of",x,"and",y, "is:",lcm(x,y))