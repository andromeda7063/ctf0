import hashlib

print("basic linux ctf")

def mdhash(x): 
    hash_object = hashlib.md5()
    hash_object.update(x.encode())
    hash_value = hash_object.hexdigest()
    
    return hash_value

def ctf(): 
    print("Flags:")
    print("1. readtheME", "2. machineZIP", "3. binary", "4. catMeIfYouCan")

    fI = int(input("enter the integer corresponding to the flag of your choice: "))

    if fI == 1:
        print("sometimes you should just read everything; or find exactly what you want")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "6c4cb797ddf535a03bf892a3e98796e6": 
                print("nice !!")
                count += 1
                done.append("1")
                flag = True
            else: 
                print("Try again")

    if fI == 2:
        print("be not afraid for windows defender will protect protect you*; your answer is one search away")
        print("*t&c apply, will NOT work if you are using the correct os (gnu/linux)")
        flag = False
        while not flag:
            a = input("enter the flag (format = flag{}): ")
            if mdhash(a) == "a370976205078d849d8f0bcb7012bac4": 
                print("congrats !!")
                count += 1
                done.append("2")
                flag = True
            else: 
                print("try again")

while True: 
    ctf()

