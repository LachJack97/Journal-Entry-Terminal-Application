
password = ""
password_confim = ""

print("Welcome to your personal journal")

def password_creation():
        password=input("You do not currently have a password set. Please enter your new password here.   ")
        password_confirm=input("Please enter your password again to confirm.   "),

if password == "":
    password_creation()
else:
    input("Please enter your password here.   ")    

print(password_confim)
print(password)

while password_confim != password:
        print("The two passwords you have entered are not the same, please try again")
        password_creation()

if password_confim == password:
        password = password_confim
        print(password)

