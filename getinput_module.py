def getinput(str, type):
    while True:
        value = input(str).strip()
        if not value: # user entered nothing
            print("\nYou entered nothing!. Pls enter a value...\n")
        else:
            if type=='int':   
                if value.isdigit(): # check if user entered a number
                    value = int(value) # convert entered number to integer
                    break
                else:
                    print("Wrong input!. You can only enter numbers.  Try again.\n")
            else:
                 break
    return value
