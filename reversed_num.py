# Find the given number by swapping its digits
# number = int(input("Enter the integer number: "))

# revs_number = 0

# while (number > 0):

#     remainder = number % 10
#     revs_number = (revs_number * 10) + remainder 
#     number = number // 10 
# print("The reverse number is: {}".format(revs_number))

# Find the given number by swapping its digits
x = 2561 
x1 = x // 1000 #2
x2 = x // 100 % 10 #5
x3 = x % 100 // 10 #6
x4 = x % 10 #1

x = x4 * 1000 + x3 * 100 + x2 * 10 + x1
print(x)
