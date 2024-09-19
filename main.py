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
    fI = int(input("Enter the integer corresponding to the flag of your choice: "))
    
    count = 0
    done = []

    if fI == 1:
        print("sometimes you should just readmd")
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
                pass    

while True: 
    ctf()

