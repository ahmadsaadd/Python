#Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
for number in range(1, 11):
    print(number)

#Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen.
#Do this first with 'for' and then with 'while' loops.
#With for
number= 11
for i in range(2, number + 1, 2):
    print(i)

#With Wile loops.
i = 2
while i <= number:
    print(i)
    i += 2

#Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values
# ​​(including the end value) on the screen.
start = 0
end = 10

for i in range(start, end + 1):
    print(i)

#Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.
number = 2

if number % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")
