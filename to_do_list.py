tasks = []
print(20*'*', "TO DO LIST" , 20*'*')
while True:
    print("1. Got new Task? 2. Completed Task? 3. Wanna See Task? 4. Bye Bye!")
    print()

    sel = int(input("enter options between 1 to 4: "))

    if sel == 1:
        what = input("what task you wanna add? :")
        tasks.append(what)
        print(what, 'is added')
        print()
        
    elif sel == 2:
        which = input("what task you wanna remove? :")
        tasks.remove(which)
        print(which, 'is removed')
        print()
        
    elif sel == 3:
        for i in tasks:
            print(i)
            print()

    elif sel == 4:
        print('Bye Bye!!! See you soon')
        break
    
    else:
        print('Wrong selection')
        print()
