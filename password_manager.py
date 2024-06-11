from cryptography.fernet import Fernet

def load_key():  #functions need to be defined before you use it UNLIKE C# where you can put them in the end
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""



def view(): #methods in c#, use "def + name()" in this case it is akin to a void method
    with open("passwords.txt", "r") as password_file: #"as password_file" is basically the name that we give the file, couldve been something else entirely
        for line in password_file.readlines():
            data = line.rstrip() #.rstrip() ignores the \n when reading, so it looks more neat and we dont see a linebreak when reading
            user, passw = data.split("|") #this looks for "|" and SPLITS the data in the .txt into array values and assigns them to user and passw.
            #since we know our .txt file contains only 2 values split by "|", we know that we only need to assign 2 values
            print("User:", user, "\nPassword:", 
                  fer.decrypt(passw.encode()).decode()) #makes the "view()" function look neater basically

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as password_file:  #opens and then closes the file in the brackets. You could use "file = open()" but you would have to manually close that one
                                #a is a mode. main modes are "w" -> creates a new file and writes. "r" -> only read file. "a" -> append mode, adds something to the END of the existing file.
        password_file.write(name + "|" + 
                            fer.encrypt(pwd.encode()).decode() + "\n") #\n linebreak, works exactly like in c#

while True:
    
    mode = input("Would you like to add a new password or view existing ones?(add, view). Press q to quit. ")

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()       
    else:
        print("Not a valid option, try again")
        continue