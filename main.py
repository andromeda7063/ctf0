import hashlib

print("basic linux ctf")

def mdhash(x): 
    hash_object = hashlib.md5()
    hash_object.update(x.encode())
    hash_value = hash_object.hexdigest()
    
    return hash_value

def ctf(): 
    print("Flags:")
    print("1.readtheME", "2.dirPandemic", "3.basicCbinary", "4.catMeIfYouCan", "5.manOfChainsaws")

    fI = input("enter the integer corresponding to the flag of your choice or type q to quit: ")

    if fI == "1":
        print("sometimes you should just read everything; or find exactly what you want")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "6c4cb797ddf535a03bf892a3e98796e6": 
                print("nice !!")
                flag = True
            else: 
                print("Try again")

    if fI == "2":
        print("be not afraid for windows defender will protect protect you*; your answer is only one search away")
        print("*t&c apply, will NOT work if you are using the correct os (gnu/linux)")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "a370976205078d849d8f0bcb7012bac4": 
                print("congrats !!")
                flag = True
            else: 
                print("try again")

    if fI == "3":
        print("help im in jail!! i cant see the lock, maybe you can")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "cf3616f9e8deff44400c2202b45e7539": 
                print("you did it !!")
                flag = True
            else: 
                print("try again")

    if fI == "4":
        print("gojo is the only one with six eyes, you might need to use them to find the flag")
        print("look deeper into the .jpg, do not stare at gojo. type hint for a hint")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "61777b63f0caac26da5448762f2497de": 
                print("cool !!")
                flag = True
            elif a == "hint":
                print("every image has a hex, find the flag")
            else: 
                print("try again")

    if fI == "5":
        print("makima is quite the manipulator, she is hiding something in the image, find the flag")
        print("type hint for a hint")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "f29d85c5fb8927fe1089c89efccae2f3": 
                print("excellent !!")
                flag = True
            elif a == "hint":
                print("images can be zips, zips can be images")
            else: 
                print("try again")

    if fI == "q":
        exit()

while True: 
    ctf()

