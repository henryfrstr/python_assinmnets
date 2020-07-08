age = input("Age: ").lower()
immune = input("immune: ").lower()
chronic = input("chronic: ").lower()

risk = age == "yes" or immune == "yes" or chronic == "yes"

if risk:
    print("You're in risk group")
else:
    print("You're not in risk group")
