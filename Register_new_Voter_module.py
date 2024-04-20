import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()
import datetime


def Register_new_Voter():
    # Table: Voter_Registration 
    while True: #Loop for accepting records
        try:
            vid='V'+datetime.datetime.now().strftime('%f')    ##  V123456
            print('\nYour Voter Id is:',vid)                
##            loopcount=1
##            while True:
##                if loopcount>2:
##                    ch=input("\nDo you want to go to main menu  y/n: ")
##                    ch=ch.upper()
##                    if ch=='Y': 
##                        return      # take user back to main menu
##
##
####                vid=getinput("\nEnter Voter ID : ", 'char')
##                
##                # If voter id exists then inform user that voterid already exists. Loop until he enters new voter id
##                if check_voter_exists(vid,'NV')==1:
##                    print("Voter already registered. Pls enter another voter ID.")
##                    loopcount=loopcount+1
##                else:
##                    break
            import getinput_module
            name=getinput_module.getinput("Enter Voter Name : ",'char')
            loopcount=1
            while True:
                adhaar=getinput_module.getinput("Enter Adhaar Number : ",'int')
                q1="select count(*) from Voter_Registration where Adhaar_Number='{}'".format(adhaar)
                mb.execute(q1)
                check=mb.fetchone()
                if check[0]==1:
                    print("\nAdhaar already in use.\n")
                else:
                    break
                loopcount=loopcount+1
                if loopcount>2:
                    ch=input("Do you want to go to voter menu  y/n: ")
                    ch=ch.upper()
                    if ch=='Y': 
                        return      # take user back to main menu

            agecount=1
            while True:
                        
                age=getinput_module.getinput("Enter Age : ",'int')
                agecount=agecount+1
                if agecount>2:
                    print("Looks like you are below 18 years. You cannot be registered as a voter... ")
                    input('\nPress any key to continue: ')
                    return
                if age<18:
                    print("Wrong input!. Value must be greater than or equal to 18. Try again.\n")
                else:
                    break
                
            parentname=getinput_module.getinput("Enter Parent or Spouse Name : ",'char')

            while True:
                gender=getinput_module.getinput("Enter Gender Male (m), Female (f): ",'char')
                gender=gender.upper()
                if gender not in('F,M'):
                    print("Wrong input!. You can only enter:  Male (m), Female (f).  Try again.\n")
                else:
                    break
            import decode_locality_module   
            locality,Assembly_constituency,Parliamentary_constituency=decode_locality_module.decode_locality()

            q1="insert into Voter_Registration values('"+name+"','"+vid+"',"+str(adhaar)+","+str(age)+",'"+parentname+"','"+gender+"','"+locality+"','"+Parliamentary_constituency+"','"+Assembly_constituency+"')"
            mb.execute(q1)
            db.commit()
            print('\nData saved successfully')

            ch=input("\nDo you want to enter more records  y/n: ")
            ch=ch.upper()
            if ch=='N':
                break

        except mysql.connector.Error as error:
            print("Failed to insert Voter record into table {}".format(error))
