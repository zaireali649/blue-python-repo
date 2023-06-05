import random

number = random.randint(0, 100)  # Generate a random number between 0 and 100
counter = 0

while number != 52:  # Repeat the following code until the number is equal to 52
    number = random.randint(0, 100)  # Generate a new random number between 0 and 100
    counter = counter + 1  # Increase the counter by 1

print(counter, number)  # Print the final counter value and the number

#######################

for i in range(10):  # Repeat the following code 10 times, with i taking values from 0 to 9
    print(i * 2)  # Print the result of multiplying i by 2

######################

number = random.randint(0, 100)  # Generate a random number between 0 and 100

for i in range(10000):  # Repeat the following code 10000 times, with i taking values from 0 to 9999
    if number == 52:  # Check if the number is equal to 52
        break  # If true, exit the loop
    else:
        number = random.randint(0, 100)  # Generate a new random number between 0 and 100

print(i, number)  # Print the value of i and the final number

######################

counter = 0

while counter < 10:  # Repeat the following code as long as the counter is less than 10
    print(counter * 2)  # Print the result of multiplying the counter by 2
    counter = counter + 1  # Increase the counter by 1

######################

number = random.randint(0, 20)  # Generate a random number between 0 and 20

for i in range(number):  # Repeat the following code a number of times equal to the value of number
    print("here")  # Print "here"

print(number)  # Print the final value of number

######################

number = random.randint(0, 20)  # Generate a random number between 0 and 20
counter = 0

while number < 20:  # Repeat the following code as long as the number is less than 20
    print("here")  # Print "here"
    number = number + 1  # Increase the number by 1
    counter = counter + 1  # Increase the counter by 1

print(counter, number)  # Print the final values of counter and number
