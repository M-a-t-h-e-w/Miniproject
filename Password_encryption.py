from cryptography.fernet import Fernet

def load_key():
    file = open("key.file","rb")
    key = file.read()
    file.close()
    return key
login_pwd = input("Provide login passcode: ")
key = load_key() + login_pwd.encode()
fer = Fernet(key)




"""
def write_key():
    key = Fernet.generate_key()
    with open("key.file","wb")as key_file:
        key_file.write(key)

write_key()"""

def load_key():
    file = open("key.file","rb")
    key = file.read()
    file.close()
    return key

def view():
    with open('password.txt','r')as f:
        for i in f.readlines():
            data = i.strip()
            user, passw = data.split("|")
            print("User:",user,"\n","password:",str(fer.decrypt(passw.encode())))
       

def add():
    name = input("Enter the your name:")
    passcode = input("Enter the your passcode:")

    with open('password.txt','a')as f:
        f.write(name +"|" + str(fer.encrypt(passcode.encode())) + "\n" )


while True:
    mode = input("Do you wanted to add the password or view the password (view or add) or press q to exit: ").lower()
    if mode== "q":
        break

    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invaild mode")
        continue