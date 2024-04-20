import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()



def declare_elections():
# this function will declare that elections can be held.
# New table Election_Status. Columns are Year, Election Type, Results declared (default is N).
# To declare elections insert one record in this table.
#There can be only oe record for one election type for which column 'Results declared' is N.
    while True: #Loop for accepting records
            try:
                import getinput_module
                year=getinput_module.getinput("\nEnter Year of election : ", 'int')
                etype=getinput_module.getinput("Enter Election Type (Parliamentary(PE) or Assembly Election(AE)): ", 'char')
                etype=etype.upper()
                #write function to check if voterid exists. If voter id exists then allow to proceed further else loop until he enters correct voter id
                q1="select count(*) from election_status where Election_Type='{}' and Results_declared='N'".format(etype)
                mb.execute(q1)
                check=mb.fetchone()
                if check[0]==1:
                    print('\nElection for Election Type',etype.upper(),'already declared. Cannot declare election again unless RESULT is declared.')
                    ch=input("\nDo you want to go to main menu.  (Y / N) ")
                    ch=ch.upper()
                    if ch=='Y': 
                        return      # take user back to main menu
                else:
                    q4="insert into election_status values("+str(year)+",'"+etype+"','N')"
                    mb.execute(q4)
                    db.commit()
                    print('\nData saved successfully')
                    ch=input("\nDo you want to enter more records y/n: ")
                    ch=ch.upper()
                    if ch=='N':
                        break
            except mysql.connector.Error as error:
                print("Failed to insert declare election record into table {}".format(error))
