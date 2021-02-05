answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")

#Practice
# True and True     T
# False and True    F
# 1 == 1 and 2 == 1     F
# "love" == "love"      T
# 1 == 1 or 2 != 1      T
# True and 1 == 1       T
# False and 0 != 0      F
# True or 1 == 1        T
# "time" == "money"     F
# 1 != 0 and 2 == 1     F
# "I Can't Believe It's Not Butter!" != "butter"        T
# "one" == 1            F
# not (True and False)      T
# not (1 == 1 and 0 != 1)   F
# not (10 == 1 or 1000 == 1000) F
# not (1 != 10 or 3 == 4)   F
# not ("love" == "love" and "time" == "money")  T
# 1 == 1 and (not ("one" == 1 or 1 == 0))   T
# "chunky" == "bacon" and (not (3 == 4 or 3 == 3))  F
# 3 == 3 and (not ("love" == "love" or "Python" == "Fun"))  F