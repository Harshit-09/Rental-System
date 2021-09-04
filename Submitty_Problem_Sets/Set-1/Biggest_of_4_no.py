numbers = []
while True:
    number = int(input("please enter a number .Enter o to finish :"))
    if number == 0:
        break
numbers.append(number)
print("maximum of {} is {}".format(numbers,max(numbers)))