import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()

def  Candidate_Nomination_by_Party():
    while True: #Loop for accepting records
        try:
            while True:
                import getinput_module
                ae_pe=getinput_module.getinput("Is nomination for Parliamentary(P) or Assembly Election(A) ? ", 'char')
                ae_pe=ae_pe.upper()
                if ae_pe=='P':
                    q1="select count(*) from election_status where Election_Type='PE'  and Results_declared='N'"
                    break
                elif ae_pe.upper()=='A':
                    q1="select count(*) from election_status where Election_Type='AE'  and Results_declared='N'"
                    break
                else:
                    print('Invalid input. You can only enter: P for Parliamentary Election or A for Assembly Election. Try again...')

            mb.execute(q1)
            check=mb.fetchone()
            if check[0]==0:
                print('\nCannot nominate Candidates unless Election is declared.\n')
                return

            while True:
                import getinput_module
                vid=getinput_module.getinput("\nEnter Voter ID of Candidate : ", 'char')
                # check if voterid exists in table Candidate_Registration. Allow user to continue only if voter id exists. Loop until he enters new voter id
                import check_voter_exists_module
                if check_voter_exists_module.check_voter_exists(vid,'NC')==0:
                    print("Candidate NOT registered. Pls enter another voter ID.")
                else:
                    break
            
            import Get_AE_PE_Name_module
            if ae_pe=='P':
                pecc=Get_AE_PE_Name_module.Get_AE_PE_Name(ae_pe)
                q3="update Candidate_Registration set PE_Contesting_Constituency='{}' where Voter_ID='{}'".format(pecc,vid)
            elif ae_pe.upper()=='A':
                aecc=Get_AE_PE_Name_module.Get_AE_PE_Name(ae_pe)
                q3="update Candidate_Registration set AE_Contesting_Constituency='{}' where Voter_ID='{}'".format(aecc,vid)
                
            mb.execute(q3)
            db.commit()
            print('\nData saved successfully')
            ch=input("\nDo you want to enter more records y/n: ")
            ch=ch.upper()
            if ch=='N':
                break
        except mysql.connector.Error as error:
            print("Failed to insert Candidate Nomination record into table {}".format(error))
            
