"""from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)"""

def view():
    print("\n")
    with open("Password_manager.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User: " + user + ", Password: " + passw)
            
def add():
    print("\n")
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("Password_manager.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")

def delete():
    view()
    with open("Password_manager.txt", "r") as f:
        lines = f.readlines()
        c = int(input("\nEnter which user/password to delete(use index): "))
        choice = input("You sure?(y/n)")

        if choice == "y":
            del(lines[c])
        with open("Password_manager.txt", "w") as f:
                f.writelines(lines)

while True:
    mode = input("\nWould you like to add a new password(a)/ view existing passwords(v)/ delete existing password(d)/ Quit(q)? ")

    if mode == "v":
        view()
    elif mode == "a":
        add()
    elif mode == "d":
        delete()
    elif mode == "q":
        break
    else:
        print("Invalid mode!")
        continue

print("\n\tThank you!")