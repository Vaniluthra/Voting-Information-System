import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()

def Close_Elections():
# this function actually updates column 'Results declared' to Y in table Election_Status.
    while True:
        try:
            q1="select * from election_status where Results_declared='N'"
            mb.execute(q1)
            ename=mb.fetchall()
            choiceno=0
            if mb.rowcount==0:
                print('\n\nAll elections are already closed...\n')
                input('Press enter to continue...\n')
                return
                    
            print('\nHere is the list of Elections that are yet to be Closed')
            print('\t YEAR\t','\t ELECTION TYPE')
            print("*"*40)
            for count in ename:
                if count[1]=='PE':
                    var='PARLIAMENTARY ELECTION'
                else:
                    var='ASSEMBLY ELECTION'
                print(choiceno+1,'\t',count[0],'\t\t',var)
                choiceno+=1
            no_of_rows=choiceno
            while True:
                import getinput_module
                choice=getinput_module.getinput("\nWhich Election do you want to Close : ", 'int')
                if choice > choiceno:
                    print('Invalid input. You can only close ELECTION 1 to',choiceno, ' Try again...')
                else:
                    break
            choiceno=1
            for count in ename:
                if choiceno==choice:
                    etype=count[1]
                    break
                else:
                    choiceno+=1
            if etype=='PE':
                q1="select count(*) from election_status where Election_Type='PE'  and Results_declared='N'"
            else:
                q1="select count(*) from election_status where Election_Type='AE'  and Results_declared='N'"
            mb.execute(q1)
            check=mb.fetchone()
            q1="update election_status set Results_declared='Y' where Election_Type='{}' and Results_declared='N'".format(etype)
            mb.execute(q1)
            db.commit()
            print(var,'is closed successfully')
            if no_of_rows>1:
                ch=input("\nDo you want to close another ELECTION (y/n) ? ")
                ch=ch.upper()
                if ch=='N':
                    break
            else:
                break
            
        except mysql.connector.Error as error:
            print("Failed to close elecion {}".format(error))
