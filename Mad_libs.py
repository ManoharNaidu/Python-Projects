print("Today, every student has a computer small enough to fit into his ___(a)[noun]___.",end = "")
print("He can solve any math problem by simply pushong the computer's little ___(b)[noun]___.",end = "")
print("Computers can add, multiply, devide, and ___(c)[verb]___.",end = "")
print("They can also ___(d)[verb]___ better than a human.Some computer are ___(e)[part of body]___ .Others have a/an ___(f)[adjective]___ screen that shows all kinds of ___(g)[noun]___ and ___(h)[adjective]___ figures.")

a = input("\nEnter ans for (a): ").lower()
b = input("\nEnter ans for (b): ").lower()
c = input("\nEnter ans for (c): ").lower()
d = input("\nEnter ans for (d): ").lower()
e = input("\nEnter ans for (e): ").lower()
f = input("\nEnter ans for (f): ").lower()
g = input("\nEnter ans for (g): ").lower()
h = input("\nEnter ans for (h): ").lower()

score = 0

if a == "bed":
    score += 1
if b == "button":
    score += 1
if c == "kill":
    score += 1
if d == "be":
    score += 1
if e == "black":
    score += 1
if f == "open":
    score += 1
if g == "cloths":
    score += 1
if h == "even":
    score += 1

print(f"\n\tYou've scored: {score}/8")
print("\n\n\n\tAnwer: ")
print(f"\nToday, every student has a computer small enough to fit into his (bed).He can solve any math problem by simply pushong the computer's little (button).Computers can add, multiply, devide, and (kill).They can also (be) better than a human.Some computer are (black).Others have a/an (open) screen that shows all kinds of (cloths) and (even) figures.")

