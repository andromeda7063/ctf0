import hashlib

print("basic linux ctf")

def mdhash(x): 
    hash_object = hashlib.md5()
    hash_object.update(x.encode())
    hash_value = hash_object.hexdigest()
    
    return hash_value

def ctf(): 
    print("Flags:")
    print("1.readtheME", "2.base64 pandemic", "3.basicCbinary", "4.catMeIfYouCan")

    fI = input("enter the integer corresponding to the flag of your choice or type q to quit: ")

    if fI == "1":
        print("sometimes you should just read everything; or find exactly what you want")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "6c4cb797ddf535a03bf892a3e98796e6": 
                print("nice !!")
                done.append("1")
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
                done.append("2")
                flag = True
            else: 
                print("try again")

    if fI == "3":
        print("help im in jail!! i cant see the lock, maybe you can")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "cf3616f9e8deff44400c2202b45e7539": 
                print("congrats !!")
                done.append("2")
                flag = True
            else: 
                print("try again")

    if fI == "4":
        print("Satoru Gojo is one of the main protagonists of the Jujutsu Kaisen series. He is a special grade jujutsu sorcerer and widely recognized as the strongest in the world. Satoru is the pride of the Gojo Clan, the first person to inherit both the Limitless and the Six Eyes in four hundred years.")
        print("look deeper into the .jpg, do not stare at gojo")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "cf3616f9e8deff44400c2202b45e7539": 
                print("congrats !!")
                done.append("2")
                flag = True
            else: 
                print("try again")


    if fI == "q":
        exit()

while True: 
    ctf()

