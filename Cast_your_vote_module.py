import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()

def  Cast_your_vote():
    try:
        q1="select * from election_status where Results_declared='N'"
        mb.execute(q1)
        value=mb.fetchall()
        if mb.rowcount==0:
            print('\n\nAll elections are closed...  No voting possible\n')
            input('Press enter to continue...\n')
            return

        for row in value:           
            if row[1]=='PE' :
                print('\n\t\t\tWELCOME TO PARLIAMENTARY ELECTION', row[0])
                import insert_vote_module
                insert_vote_module.insert_vote(row, "\nContinue Voting for Parliamentary Elections ? y/n: ")
            elif row[1]=='AE' :
                print('\n\n\t\t\tWELCOME TO ASSEMBLY ELECTION', row[0])
                import insert_vote_module
                insert_vote_module.insert_vote(row, "\nContinue Voting for Assembly Elections ? y/n: ")    
        
    except mysql.connector.Error as error:
        print("Failed to insert Vote Casting record into table {}".format(error))
