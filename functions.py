def greet(name):
    return f"Hi {name}!"

print(greet('Cristian'))
print("")

#---------------

def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(28))
print("")

#-----------------
def sum_product(num1, num2):
    return print(f"the sum is {num1 + num2}, and product is {num1 * num2}")

sum_product(2, 4)
print("")

#----------------
# Create a function called uppercase_and_reverse that takes a little bit of text, uppercases it all, and then reverses it (flips all the letters around) so that:

def uppercase_and_reverse(word):
    return word.upper()[::-1]

print(uppercase_and_reverse("Banana"))
print("")
