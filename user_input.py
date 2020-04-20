print("İf you forgot your password please follow instructions...")
name = input("Please Enter your name: ").lower().strip()

if name == "henry":
    print("Hello, {}! The password is asd@123*".format(name.capitalize()))
else:
    print("Hello {}! See you later.")