#Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
print("Question 1")
for number in range(1, 11):
    print(number)
print("--------------------------------------------")
#Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen.
#Do this first with 'for' and then with 'while' loops.
#With for
print("Question 2")
number= 11
for i in range(2, number + 1, 2):
    print(i)

#With Wile loops.
i = 2
while i <= number:
    print(i)
    i += 2
print("--------------------------------------------")
#Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values
# ​​(including the end value) on the screen.
print("Question 3")
start = 0
end = 10

for i in range(start, end + 1):
    print(i)
print("--------------------------------------------")
#Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.
print("Question 4")
number = 3

if number % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")
print("--------------------------------------------")
#Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial.
#Factorial is the product of all positive integers between a number itself and 1.
# For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120
print("Question 5")
number = 4
if number < 0:
    print("Please enter a positive integer.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial:", factorial)
print("--------------------------------------------")

