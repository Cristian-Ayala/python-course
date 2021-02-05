the_count = [1,2,3,4,5]
stocks = ["AAPL", "GOOG", "TSLA"]
ramdom_thing = ["Purple", 55, "Cristian Ayala", 1/2,["This"," is","a list"]]

for number in the_count:
    print("This is the cout:", number)

print("")

for stock in stocks:
    print("Stock ticker:", stock)

print("")

for thing in ramdom_thing:
    print("Here is a ramdom thing", thing)

print("")

#index looping
ram_list = ["blah", 1, 3.1415, {1, 1, 1}]

for i in range(len(ram_list)):
  print(f"list position {i}: {ram_list[i]}")

print("")

#-------------------------------------------------------------------------

# we can also build lists, first let's start with an empty one
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)

print("")

#-------------------------------------------------------------------------
# Challenge: Print out the square of the numbers 1 to 10

for number in range(1,11):
    print(number, "squared is", number ** 2)

print("")

#-------------------------------------------------------------------------
#Get last element
another_list = random_things[-1]