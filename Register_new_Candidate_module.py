import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()
import datetime



def  Register_new_Candidate():
    # Table : Candidate_Registration. Record insert - 
    while True: #Loop for accepting records 
        try:
            loopcount=1
            while True:
                if loopcount>2:
                    ch=input("\nDo you want to go to main menu  y/n: ")
                    ch=ch.upper()
                    if ch=='Y': 
                        return      # take user back to main menu
                import getinput_module
                vid=getinput_module.getinput("\nEnter Voter ID of Candidate : ", 'char')
                # check if voterid exists in table Candidate_Registration. If voter id exists then inform user that voterid already exists. Loop until he enters new voter id
                import check_voter_exists_module
                if check_voter_exists_module.check_voter_exists(vid,'NC')==1:
                    print("Candidate already registered. Pls enter another voter ID.")
                else:
                # check if voterid exists in table Voter_Registration. If voter id does not exists then inform user to enter registered voter id only. Loop until he enters correct voter id
                    if check_voter_exists_module.check_voter_exists(vid,'NV')==0:
                        print("Candidate NOT registered as a voter.")
                    else:
                        break
                loopcount=loopcount+1
            q1="select Voter_Name from Voter_Registration where Voter_ID='{}'".format(vid)
            mb.execute(q1)
            name=mb.fetchone()
            pname=getinput_module.getinput("Enter Party Name : ", 'char')
            psname=getinput_module.getinput("Enter Party Symbol Name : ", 'char')
            q2="insert into Candidate_Registration values('"+vid+"','"+name[0]+"','','','"+pname+"','"+psname+"')"
            mb.execute(q2)
            db.commit()
            print('\nData saved successfully')

            ch=input("\nDo you want to enter more records  y/n: ")
            ch=ch.upper()
            if ch=='N':
                break
            
        except mysql.connector.Error as error:
            print("Failed to insert Candidate record into table {}".format(error))
