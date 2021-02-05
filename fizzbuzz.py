# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)


#-----------------------------
print("")

#FizzBuzz in 1 lines
for i in range(1, 101): print("FizzBuzz" if i%5==0 and i%3==0 else "Fizz" if i% 3==0 else "Buzz" if i%5 == 0 else i)