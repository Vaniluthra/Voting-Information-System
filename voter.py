def voterfunc(theinput):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='root',password='12345$',database='voterdb')
    mb=db.cursor()

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


    def decode_locality():
            print("Tell us where you reside. Choose one of the following.")
            print("Rohini : 1\tRithala : 2\tPitamPura/Shalimar Bagh: 3\tBawana : 4\tBurari: 5\tMangol Puri : 6\tBadli : 7\tVikaspuri : 8\tJanakpuri : 9\tShakur Basti : 10")
            ch=int(input("Enter Locality : "))
            while True:
                if ch==1:
                      locality='Rohini'
                      Assembly_constituency='Rohini'
                      Parliamentary_constituency='North West Delhi'
                      break
                elif ch==2:
                      locality='Rithala'
                      Assembly_constituency='Rithala'
                      Parliamentary_constituency='North West Delhi'
                      break
                elif ch==3:
                      locality='Shalimar Bagh'
                      Assembly_constituency='Shalimar Bagh'
                      Parliamentary_constituency='Chandni Chowk'
                      break
                elif ch==4:
                      locality='Bawana'
                      Assembly_constituency='Bawana'
                      Parliamentary_constituency='North West Delhi'
                      break
                elif ch==5:
                      locality='Burari'
                      Assembly_constituency='Burari'
                      Parliamentary_constituency='North East Delhi'
                      break
                elif ch==6:
                      locality='Mangol Puri'
                      Assembly_constituency='Mangol Puri'
                      Parliamentary_constituency='North West Delhi'
                      break
                elif ch==7:
                      locality='Badli'
                      Assembly_constituency='Badli'
                      Parliamentary_constituency='North West Delhi'
                      break
                elif ch==8:
                      locality='Vikaspuri'
                      Assembly_constituency='Vikaspuri'
                      Parliamentary_constituency='West Delhi'
                      break
                elif ch==9:
                      locality='Janakpuri'
                      Assembly_constituency='Janakpuri'
                      Parliamentary_constituency='West Delhi'
                      break
                elif ch==10:
                      locality='Shakur Basti'
                      Assembly_constituency='Shakur Basti'
                      Parliamentary_constituency='Chandni Chowk'
                      break
                else:
                    print('Invalid input..try again')
            return locality,Assembly_constituency,Parliamentary_constituency

    def check_voter_exists(voterid,table):
        try:
            if table=='NV':
                q1="select count(Voter_ID) from Voter_Registration where Voter_ID='{}'".format(voterid)
                mb.execute(q1)
                check=mb.fetchone()
            elif table=='NC':
                q1="select count(Voter_ID) from Candidate_Registration where Voter_ID='{}'".format(voterid)
                mb.execute(q1)
                check=mb.fetchone()

        except mysql.connector.Error as error:
                print("Failed to verify if Voter exists {}".format(error))        

        return check[0]
    def mod_menu():
        print("\n\t\t\tModify Menu:\n")
        print("*"*70)
        print("1-To modify Voter's name")
        print("2-To modify Age")
        print("3-To modify Parent's or Spouse's Name")
        print("4-To modify Locality")
        print("5-To modify Parliamentary constituency")
        print("6-To modify Assembly constituency")
        print("7-Exit")
    def voter_modify():
        a=0
        q="Select * from voter_registration"
        mb.execute(q)
        f=mb.fetchall()
        vid=getinput("Enter Voter ID to modify record: ",'char')
        if check_voter_exists(vid,"NV")==1:
            for i in f:
                if i[1]==vid:
                    mod_menu()
                    ch=input("Enter your choice: ")
                    if ch=='1':
                        vname=input("Enter new name: ")
                        q="Update voter_registration set Voter_name='%s' where voter_id='%s'"%(vname,vid)
                        mb.execute(q)
                        db.commit()
                        print("Voter name modified")
                        a+=1
                    elif ch=='2':
                        age=int(input("Enter new age: "))
                        q="Update voter_registration set age='%s' where voter_id='%s'"%(age,vid)
                        mb.execute(q)
                        db.commit()
                        print("Voter's age modified")
                        a+=1
                    elif ch=='3':
                        pars=input("Enter parent/spouse name: ")
                        q="Update voter_registration set parent_or_spouse_name='%s' where voter_id='%s'"%(pars,vid)
                        mb.execute(q)
                        db.commit()
                        print("Parent/Spouse name modified")
                        a+=1
                    elif ch=='4':
                        loc=input("Enter new locality: ")
                        q="Update voter_registration set locality='%s' where voter_id='%s'"%(loc,vid)
                        mb.execute(q)
                        db.commit()
                        print("Locality modified")
                        a+=1
                    elif ch=='5':
                        pc=input("Enter new parlimentary contituency: ")
                        q="Update voter_registration set parliamentary_constituency='%s' where voter_id='%s'"%(pc,vid)
                        mb.execute(q)
                        db.commit()
                        print("Parliamentary constituency modified")
                        a+=1
                    elif ch=='6':
                        ac=input("Enter new assembly contituency: ")
                        q="Update voter_registration set assembly_constituency='%s' where voter_id='%s'"%(ac,vid)
                        mb.execute(q)
                        db.commit()
                        print("Assembly constituency modified")
                        a+=1
                    elif ch=='7':
                        break
                    else:
                        print("Enter valid choice from 'Modify Menu'")
                        voter_modify()
        else:
            print("Voter ID does not exists")
            voter_modify()
            
    def voter_delete():
        vid=getinput('\nEnter Voter ID to be deleted : ','char')
        if check_voter_exists(vid,"NV")==1:
        
            q="Delete from voter_registration where voter_id='%s'"%(vid)
            mb.execute(q)
            db.commit()
            print('Data deleted successfully...\n')
            q='select * from voter_registration'
            mb.execute(q)
            abc=mb.fetchall()
            
            for i in abc:
                print("%10s"%i[0],"%15s"%i[1],"%15s"%i[2],"%5s"%i[3],"%15s"%i[4],"%5s"%i[5],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8])
            q='select * from voter_registration'
            mb.execute(q)
            
        else:
            print("Voter ID does not exist")
            voter_delete()

    if theinput=='2':
        voter_modify()
    elif theinput=='3':
        voter_delete()
    

