print("İf you forgot your password please follow instructions...")
name = input("Please Enter your name: ").capitalize().strip()

if name == "Henry":
    print("Hello, {}! The password is asd@123*".format(name))
else:
    print("Hello {}! See you later.".format(name))