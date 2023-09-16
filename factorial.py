#code for computing factorial
num1 = int(input('please enter a number'))
result = 1
if num1 < 0:
    print('error! number less than 0')
elif num1 == 0:
    print('factorial of 0 is 1')
else:
    for i in range(1, num1+1):
        result = result * i
    print('Factorial of', num1 , "is" , result)