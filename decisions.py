import random

number = random.randint(0, 10)  # Generate a random number between 0 and 10 (inclusive)

threshold = 5  # Set the threshold value to 5

if number > 8:  # Check if the number is greater than 8
    print("very big number")  # If true, print "very big number"
elif number > threshold:  # If the number is not greater than 8, check if it's greater than the threshold (5)
    print("big number")  # If true, print "big number"
    print("big number")
    print("big number")
elif number < threshold:  # If the number is not greater than the threshold, check if it's smaller
    print("small number")  # If true, print "small number"
elif number == threshold:  # If the number is not smaller than the threshold, check if it's equal to the threshold
    print("number equal", threshold)  # If true, print "number equal" followed by the threshold value

if number > 4:  # Check if the number is greater than 4
    print("number is greater than 4")  # If true, print "number is greater than 4"

print(number)  # Print the generated random number
