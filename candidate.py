def candfunc(theinput):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='root',password='12345$',database='voterdb')
    mb=db.cursor()

    #modify candidate info
    #with change1

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
            print("\n\n\t\t\t\t\t\t\t    Choose one of the following.     ")
            print("Rohini : 1\nRithala : 2\nPitamPura/Shalimar Bagh: 3\nBawana : 4\nBurari: 5\nMangol Puri : 6\nBadli : 7\nVikaspuri : 8\nJanakpuri : 9\nShakur Basti : 10")
            ch=int(input("\n\n\nEnter new Locality : "))
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
                q1="select count(Voter_ID) from voter_registration where Voter_ID='{}'".format(voterid)
                mb.execute(q1)
                check=mb.fetchone()
            elif table=='NC':
                q1="select count(Voter_ID) from candidate_registration where Voter_ID='{}'".format(voterid)
                mb.execute(q1)
                check=mb.fetchone()

        except mysql.connector.Error as error:
                print("Failed to verify if Voter exists {}".format(error))
#        print(check[0])

        return check[0]


    def mod_menu1():
        print('\n')
        print("*"*70)
        print("\n\t\t\tModify Menu\n")
        print("1. To modify Candidate's name")
        print("2. To modify Age")
        print("3. To modify Parent's or Spouse's Name")
        print("4. To modify Locality")
        print("5. To modify Parliamentary constituency")
        print("6. To modify Assembly constituency")
        print("7. To modify Parliamentaty Election Contesting Constituency")
        print("8. To modify Assembly Election Contesting Constituency")
        print("9. Go back to Candidate Menu\n")
        print("*"*70)



    def cand_modify():
        a=0
        q="Select * from candidate_registration"
        mb.execute(q)
        f=mb.fetchall()
        import getinput_module
        cid=getinput_module.getinput("\nEnter Candidate ID to modify record: ",'char')
        import check_voter_exists_module
        if check_voter_exists_module.check_voter_exists(cid,"NC")==1:

            for i in f:
                
                if i[0]==cid:
                    
                    mod_menu1()
                    ch=input("\nEnter your choice: ")
                    if ch=='1':
                        cname=input("\nEnter new name: ")
                        q="Update voter_registration set Voter_Name='%s' where voter_id='%s'"%(cname,cid)
                        mb.execute(q)
                        db.commit()
                        q1="Update candidate_registration set Voter_Name='%s' where voter_id='%s'"%(cname,cid)
                        mb.execute(q1)
                        db.commit()
                        print("Candidate name modified")
                        a+=1
                    elif ch=='2':
                        age=int(input("\nEnter new age: "))
                        q="Update voter_registration set age='%s' where voter_id='%s'"%(age,cid)
                        mb.execute(q)
                        db.commit()
                        print("Candidate's age modified")
                        a+=1
                    elif ch=='3':
                        pars=input("\nEnter parent/spouse name: ")
                        q="Update voter_registration set parent_or_spouse_name='%s' where voter_id='%s'"%(pars,cid)
                        mb.execute(q)
                        db.commit()
                        print("Parent/Spouse name modified")
                        a+=1
                    elif ch=='4':
                        loc=input("\nEnter new locality: ")
                        q="Update voter_registration set locality='%s' where voter_id='%s'"%(loc,cid)
                        mb.execute(q)
                        db.commit()
                        print("Locality modified")
                        a+=1
                    elif ch=='5':
                        m=decode_locality()
                        q="Update voter_registration set parliamentary_constituency='%s' where voter_id='%s'"%(m[2],cid)
                        mb.execute(q)
                        db.commit()
                        print("Parliamentary constituency modified")
                        a+=1
                    elif ch=='6':
                        m=decode_locality()
                        q="Update voter_registration set assembly_constituency='%s' where voter_id='%s'"%(m[1],cid)
                        mb.execute(q)
                        db.commit()
                        print("Assembly constituency modified")
                        a+=1
                    elif ch=='7':
                        m=decode_locality()
                        q="Update candidate_registration set PE_Contesting_Constituency='%s' where voter_id='%s'"%(m[2],cid)
                        mb.execute(q)
                        db.commit()
                        print("Parliamentary Election contesting constituency modified")
                        a+=1
                    elif ch=='8':
                        m=decode_locality()
                        q="Update candidate_registration set AE_Contesting_Constituency='%s' where voter_id='%s'"%(m[1],cid)
                        mb.execute(q)
                        db.commit()
                        print("Assembly Election contesting constituency modified")
                        a+=1
                        
                        
                    elif ch=='9':
                        break
                    else:
                        print("Enter valid choice from 'Modify Menu'")
                        cand_modify()
        else:
            print("Candidate ID does not exists...")
            cand_modify()


    #delete candidate

    def cand_delete():

        import getinput_module
        cid=getinput_module.getinput('\nEnter Candidate ID to be deleted : ','char')
        import check_voter_exists_module
        if check_voter_exists_module.check_voter_exists(cid,"NV")==1:
            q="Delete from candidate_registration where Voter_ID='%s'"%(cid)
            mb.execute(q)
            db.commit()
            print('Data deleted successfully...\n')
        else:
            print("Candidate ID does not exist...")
            cand_delete()


    if theinput=='3':
        cand_modify()
    elif theinput=='4':
        cand_delete()
    

















