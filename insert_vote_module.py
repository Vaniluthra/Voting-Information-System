import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()


def  insert_vote(row,string):
    while True:
        import getinput_module
        vid=getinput_module.getinput("\nEnter your Voter ID : ", 'char')
        # Check if voter has already voted or not
        q1="select count(Voter_ID) from  Voting_Details where Voter_ID='{}' and Election_Type='{}' and Year='{}' and Vote_Count=0".format(vid,row[1],row[0])
        mb.execute(q1)
        check=mb.fetchone()
        if check[0]>=1:     # if voter has voted then take him to main menu
            print("You have already voted. Cannot vote again.\n")
        else:
            # Get list of candidates : voterid, party name, voter name of candidates contesting in voter's constituency
            if row[1]=='PE' :
                q1="select Party_Name,b.Voter_Name,b.Voter_ID from voter_registration a,candidate_registration b where Parliamentary_Constituency=PE_Contesting_Constituency and a.Voter_ID='{}'".format(vid)                
            else:
                q1="select Party_Name,b.Voter_Name,b.Voter_ID from voter_registration a,candidate_registration b where Assembly_Constituency=AE_Contesting_Constituency and a.Voter_ID='{}'".format(vid)
            mb.execute(q1)
            cname=mb.fetchall()
            choiceno=0
            if mb.rowcount==0:      # No candidates so cannot vote 
                print('\n\nThere are no candidates contesting in your constituency...\n')
                input('Press enter to continue...\n')
            else:                   # Voter can vote
                print('\nHere is the list of Candidates contesting in your constituency')
                print('%30s'% 'PARTY NAME','%30s'%'CANDIDATE NAME')
                print("*"*60)
                for count in cname:
                    print(choiceno+1,'%30s'%count[0].upper(),'%30s'%count[1].upper())
                    choiceno+=1
                
                while True: 
                    vote=getinput_module.getinput("\nEnter your Vote : ", 'int')
                    if vote > choiceno:
                        print('Invalid input. You can only vote for candidate 1 to',choiceno, ' Try again...')
                    else:
                        break
                q1="insert into Voting_Details values('"+vid+"',"+str(row[0])+",'"+row[1]+"',0)"
                mb.execute(q1)
                db.commit()
                print('\nThank you for Voting.\n')
                choiceno=1
                for count in cname:
                    if choiceno==vote:
                        cid=count[2]
                        break
                    else:
                        choiceno+=1
                # Check if candidate  has already been voted or not
                q1="select count(Voter_ID) from  Voting_Details where Voter_ID='{}' and Election_Type='{}' and Year='{}' and Vote_Count>=1".format(cid,row[1],row[0])
                mb.execute(q1)
                check=mb.fetchone()
                if check[0]==1 :     # if voter has voted then update his vote count
                    q1="update Voting_Details set Vote_Count=Vote_Count+1 where Voter_ID='{}' and Election_Type='{}' and Year='{}' and Vote_Count!=0".format(cid,row[1],row[0])
                    mb.execute(q1)
                    db.commit()
                else:
                    q1="insert into Voting_Details values('"+cid+"',"+str(row[0])+",'"+row[1]+"',1)"
                    mb.execute(q1)
                    db.commit()

        ch=input(string)        # check if user wants to continue with this election type
        ch=ch.upper()
        if ch=='N':
            break
