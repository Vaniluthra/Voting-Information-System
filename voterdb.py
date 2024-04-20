
import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()
import datetime


def Menu(): #Function to display the menu
    print('\n\t\t\t\t\t\t\t  Version: 1.5')
    print("*"*70)
    print("\n\t\t\t\tMAIN MENU\n")
    print("\t\t1. Voter")
    print("\t\t2. Candidate")
    print("\t\t3. Elections")
    print("\t\t4. Reports")
    print("\t\t5. Exit\n")   
    print("*"*70)


def voter_menu(): #Function to display the voter menu
    print('\n')
    print("*"*70)
    print("\n\t\t\t\tVOTER MENU\n")
    print("\t\t1. Register new Voter")
    print("\t\t2. Modify Voter Information")
    print("\t\t3. Delete Voter")
    print("\t\t4. Go back to Main Menu\n")
    print("*"*70)

def candidate_menu(): #Function to display the candidate menu
    print('\n')
    print("*"*70)
    print("\n\t\t\t\tCANDIDATE MENU\n")
    print("\t\t1. Register new Candidate")
    print("\t\t2. Candidate Nomination by Party")
    print("\t\t3. Modify Candidate Information")
    print("\t\t4. Delete Candidate")
    print("\t\t5. Go back to Main Menu\n")
    print("*"*70)

def election_menu(): #Function to display the election menu
    print('\n')
    print("*"*70)
    print("\n\t\t\t\tELECTION MENU\n")
    print("\t\t1. Declare Elections")
    print("\t\t2. Cast your vote")
    print("\t\t3. Close Elections")
    print("\t\t4. Go back to Main Menu\n")
    print("*"*70)

def report_menu(): #Function to display the report menu
    print('\n')
    print("*"*70)
    print("\n\t\t\t\tREPORTS MENU\n")
    print("\t\t1. Voter Information")
    print("\t\t2. Voting Information")
    print("\t\t3. Go back to Main Menu\n")    
    print("*"*70)


def  Close_all():
        if (db.is_connected()):
            mb.close()
            db.close()
            print("\nThanks for using the Voter Information System\n")

            
while True:
    Menu()
    ch=input("\nEnter your Choice : ")

    if ch=="1":
        while True:
            voter_menu()
            chv=input("\nEnter your Choice : ")
            if chv=="1":
                import Register_new_Voter_module 
                Register_new_Voter_module.Register_new_Voter()
            elif chv=="2":
                from voter import voterfunc     
                voterfunc(chv)
            elif chv=="3":
                from voter import voterfunc
                voterfunc(chv)
            else:
                break

    elif ch=="2":
        while True:
            candidate_menu()
            chc=input("\nEnter your Choice : ")
            if chc=="1":
                import Register_new_Candidate_module
                Register_new_Candidate_module.Register_new_Candidate()
            elif chc=="2":
                import Candidate_Nomination_by_Party_module
                Candidate_Nomination_by_Party_module.Candidate_Nomination_by_Party()
            elif chc=="3":
                from candidate import candfunc
                candfunc(chc)
            elif chc=="4":
                from candidate import candfunc
                candfunc(chc)
            else:
                break

    elif ch=="3":
        while True:
            election_menu()
            che=input("\nEnter your Choice : ")
            if che=="1":
                import declare_elections_module
                declare_elections_module.declare_elections()
            elif che=="2":
                import Cast_your_vote_module
                Cast_your_vote_module.Cast_your_vote()
            elif che=="3":
                import Close_Elections_module
                Close_Elections_module.Close_Elections()
            else:
                break
            
    elif ch=="4":
        while True:
            report_menu()
            chrm=input("\nEnter your Choice : ")
            if chrm=="1":
                import reports_sanya
                reports_sanya.mainfunction1()
            elif chrm=="2":
                import reports_vidhi
                reports_vidhi.mainfunction2()
            else:
                break
            
    else:
        Close_all()
        break
