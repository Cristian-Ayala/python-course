# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)
import os
# start with a blank screen
os.system('clear')                       
total = float(input("What is you're bill sub-total? ").strip('$'))

print("Tip Suggestions:")
print("----------------")
print(f"15% is ${total * 0.15:.2f}")
print(f"18% is ${total * 0.18:.2f}")
print(f"20% is ${total * 0.20:.2f}")