def mainfunction2():
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='root',password='12345$',database='voterdb')
    mb=db.cursor()

    #####################################################           FUNCTIONS             #######################################################################

    #MENU

    def Menu():
        print("*"*70)
        print("\n\t\t\tVOTING INFORMATION MENU\n")
        print("1. Comparison of turn outs")
        print("2. Candidate voting information")
        print("3. Winner Declaration")
        print("4. Votes received by each candidate\n")
        print("Press any other number key to return to main menu")
        print("*"*70)

    def getinput(str, type):
        while True:
            value = input(str).strip()
            if not value:
                print("\nYou entered nothing!. Pls enter a value...\n")
            else:
                if type=='int':   
                    if value.isdigit(): 
                        value = int(value) 
                        break
                    else:
                        print("Wrong input!. You can only enter numbers.  Try again.\n")
                else:
                     break
        return value

    #number of voters
    def totalvoters():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        q='select count(*) from voter_registration'
        mb.execute(q)
        f=mb.fetchone()
        return f[0]


    #number of votes for a year
    def votecount(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        q='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voting_details.year={}'.format(year)
        mb.execute(q)
        f=mb.fetchone()
        return f[0]

    #turn out for a year
    def turnout(year):
        
        t=totalvoters()
        v=votecount(year)
        turnout=(v/t)*100
        if t!=0:
            turnout=int((v/t)*100)
        else:
            print("No voter registered!")
        return turnout

    #number of people who voted in parliamentary elections

    def parliamentaryvotes():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        pvote=[]
        pcon=['North West Delhi', 'Chandini Chowk', 'West Delhi']
        ptotal=0
        for i in pcon:
            q="select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.parliamentary_constituency='{}'".format(i)
            mb.execute(q)
            f=mb.fetchall()
            pvote.append(f[0][0])
        for i in range(len(pvote)):
            ptotal+=i
        return ptotal    

    # number of people who voted in assembly elections

    def assemblyvotes():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        avote=[]
        acon=['Rohini', 'Rithala', 'Pitampura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Vikaspuri','Janakpuri','Shakur Basti',]
        atotal=0
        for i in acon:
            q="select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.assembly_constituency='{}'".format(i)
            mb.execute(q)
            f=mb.fetchall()
            avote.append(f[0][0])
        for i in range(len(avote)):
            atotal+=i
        return atotal

    #list of years
    def year():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        year=[]
        q="select year,count(*) from voting_details group by year"
        mb.execute(q)
        f=mb.fetchall()
        for i in range(len(f)):
            year.append(f[i][0])
        return year


    ##Comparison of turnouts

    #On basis of year

    def comp_year():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        yturnout=[]
        yearlist=year()
        for i in yearlist:
            y=turnout(i)
            yturnout.append(y)
        return yturnout

    #On basis of PE and AE

    def comp_ae_pe():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        pe=parliamentaryvotes()
        ae=assemblyvotes()
        if pe>ae:
            print("\n\t\t\tPeople voted more in Assembly elections!\n")
        elif ae>pe:
            print("\n\t\t\tPeople voted more in Parliamentary elections!\n")
        else:
            print("\n\t\t\tPeople voted in both Assembly and Parliamentary elections equally!\n")


    ##Votes of candidates

    #list of candidates
    def candidate_list(year,pe_ae):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        q="Select candidate_registration.voter_id from voting_details,candidate_registration where candidate_registration.voter_id=voting_details.voter_id and year={} and election_type='{}'".format(year,pe_ae)
        mb.execute(q)
        f=mb.fetchall()
        candlist=[]
        for i in f:
            q1="Select * from candidate_registration where voter_id='{}'".format(i[0])
            mb.execute(q1)
            f1=mb.fetchone()
            candlist.append(f1)
        return candlist

    #maximum votes received by candidate

    ##counstituency wise

    #parliamentary constituencies

    def pe_candidate(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        pcon=['North West Delhi', 'Chandini Chowk', 'West Delhi']
        votecount=[]
        for i in pcon:
            q="select party_name,max(vote_count) from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and pe_contesting_constituency='{}' and year={}".format(i,year)
            mb.execute(q)
            f=mb.fetchone()
            votecount.append(f[0])
        return votecount

    #assembly constituencies

    def ae_candidate(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        acon=['Rohini', 'Rithala', 'Pitampura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Vikaspuri','Janakpuri','Shakur Basti']
        votecount=[]
        for i in acon:
            q="select party_name,max(vote_count) from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and ae_contesting_constituency='{}' and year={}".format(i,year)
            mb.execute(q)
            f=mb.fetchone()
            votecount.append(f[0])
        return votecount

    ## election type wise
    def candidate_election(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        elist=["PE", "AE"]
        votecount=[]
        for i in elist:
            q="select voter_id,max(vote_count) from voting_details where year={} and election_type='{}'".format(year,i)
            mb.execute(q)
            f=mb.fetchone()
            votecount.append(f[0])
        return votecount
                            
    ##gender wise

    #female winners



       
    def female_candidate():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
         #total female candidates
        q="select candidate_registration.voter_id from candidate_registration,voter_registration where candidate_registration.voter_id=voter_registration.voter_id and gender='F'"
        mb.execute(q)
        flist=mb.fetchone()
        ftotal=0
        for i in flist:
            ftotal+=1
        #female candidate who won election

        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        q1="select candidate_registration.voter_id,max(vote_count) from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id group by year"
        mb.execute(q1)
        f1=mb.fetchall()
        fcount=0
        for i in range(len(f1)):
            if f1[i][0] in flist:
                fcount+=1
        return [ftotal,fcount]

    # male winners

    def male_candidate():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        #total male candidates
        q="select candidate_registration.voter_id from candidate_registration,voter_registration where candidate_registration.voter_id=voter_registration.voter_id and gender='M'"
        mb.execute(q)
        mlist=mb.fetchone()
        mtotal=0
        for i in mlist:
            mtotal+=1

        #male candidate who won election

        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        
        q1="select candidate_registration.voter_id,max(vote_count) from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id group by year"
        mb.execute(q1)
        f1=mb.fetchall()
        mcount=0
        for i in range(len(f1)):
            if f1[i][0] in mlist:
                mcount+=1
        return [mtotal,mcount]

            

    #Winner Declaration

    def winner(year,pe_ae):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        q="select party_name,max(vote_count) from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and year={} and election_type='{}'".format(year,pe_ae)
        mb.execute(q)
        winner=mb.fetchall()
        if pe_ae=='PE':
            print("\n\t\t\t\tTHE WINNER OF PARLIAMENTARY ELECTIONS",year,"IS")
            print("\t\t\t\t\t\t",winner[0][0])
        elif pe_ae=='AE':
            print("\n\t\t\t\tTHE WINNER OF ASSEMBLY ELECTIONS",year,"IS")
            print("\t\t\t\t\t\t",winner[0][0])
            
    #vote got by each candidate

    #constituency wise
            
    #parliamentary constituencies

    def pe_candidate_vote(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        pcon=['North West Delhi', 'Chandini Chowk', 'West Delhi']
        votecount=[]
        for i in pcon:
            q="select party_name,vote_count from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and pe_contesting_constituency='{}' and year={}".format(i,year)
            mb.execute(q)
            f=mb.fetchall()
            votecount.append(f)
        return votecount


    #assembly constituency
    def ae_candidate_vote(year):
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        acon=['Rohini', 'Rithala', 'Pitampura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Vikaspuri','Janakpuri','Shakur Basti']
        votecount=[]
        for i in acon:
            q="select party_name,vote_count from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and ae_contesting_constituency='{}' and year={}".format(i,year)
            mb.execute(q)
            f=mb.fetchall()
            votecount.append(f)
        return votecount



    ## Year wise

    def year_candidate_vote():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        yearlist=year()
        votecount=[]
        for i in yearlist:
            q="select voter_name,vote_count from candidate_registration,voting_details where candidate_registration.voter_id=voting_details.voter_id and year={}".format(i)
            mb.execute(q)
            f=mb.fetchall()
            votecount.append(f)
        return votecount


    ###########################################################################  INPUTS #####################################################################################
    yearlist=year()

    while True:
        print("*"*70)
        print("\n\t\t\tVOTING INFORMATION MENU\n")
        print("1. Comparison of turn outs")
        print("2. Candidate voting information")
        print("3. Winner Declaration")
        print("4. Votes received by each candidate\n")
        print("*"*70)
        ch=getinput("Enter choice from menu: ","int")
        if ch==1:
            print("\n\t\t\t1-Constituency Wise")
            print("\t\t\t2-Year wise\n")
            inp=getinput("Enter your choice(1/2): ","int")
            if inp==1:
                comp_ae_pe()
            elif inp==2:
                yturnout=comp_year()
                yearlist=year()
                print("-"*150)
                print("\n%10s"%"Year","%40s"%"Turn Out")
                print("-"*150)
                for i in range(len(yearlist)):
                    print("%10s"%yearlist[i],"%40s"%yturnout[i])
            else:
                ("\n\t\t\tENTER VALID CHOICE!!!\n")
        elif ch==2:
            print("\n\t\t\t1-Constituency wise")
            print("\t\t\t2-Gender wise(Male-Female Ratio)")
            inp=getinput("\nEnter your choice(1/2): ","int")
            if inp==1:
                print("\n\t\t\t1-Parliamentary Constituency")
                print("\t\t\t2-Assembly Constituency")
                inp1=getinput("\nEnter your choice(1/2): ","int")
                if inp1==1:
                    year=getinput("Enter year","int")
                    pcon=['North West Delhi', 'Chandini Chowk', 'West Delhi']
                    if year in yearlist:
                        pe_candidate=pe_candidate(year)
                        print("-"*150)
                        print("\n%20s"%"Constituency","%40s"%"Winner")
                        print("-"*150)
                        for i in range(len(pcon)):
                            print("%20s"%pcon[i],"%40s"%pe_candidate[i])
                elif inp1==2:
                    year=getinput("Enter year: ","int")
                    acon=['Rohini', 'Rithala', 'Pitampura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Vikaspuri','Janakpuri','Shakur Basti']
                    if year in yearlist:
                        ae_candidate=ae_candidate(year)
                        print("-"*150)
                        print("\n%25s"%"Constituency","%40s"%"Winner")
                        print("-"*150)
                        for i in range(len(acon)):
                            print("%25s"%acon[i],"%40s"%ae_candidate[i])
                else:
                    print("\n\t\t\t\t\tINVALID INPUT\n")
            elif inp==2:
                m=male_candidate()
                mtotal=m[0]
                mwin=m[1]
                f=female_candidate()
                ftotal=f[0]
                fwin=f[1]
                print("-"*150)
                print("\n%20s"%"Gender","%40s"%"Number of candidates","%40s"%"Number of candidates who won")
                print("-"*150)
                print("%20s"%"Male","%40s"%mtotal,"%40s"%mwin)
                print("%20s"%"Female","%40s"%ftotal,"%40s"%fwin)
            else:
                print("\n\t\t\t\t\tINVALID INPUT\n")     
        elif ch==3:
            print("\n\t\t\t1-Parliamentary Elections")
            print("\t\t\t2-Assembly Elections")
            inp=getinput("Enter your choice(1/2): ","int")
            if inp==1:
                year=getinput("Enter year: ","int")
                if year in yearlist:
                    q='select results_declared from election_status where election_type="pe"'
                    mb.execute(q)
                    f=mb.fetchone()
                    if f[0] in 'Yy':
                        winner(year,"PE")
                    else:
                        print("\n\t\t\tRESULTS NOT DECLARED\n")
                else:
                    print("\n\t\t\t\t\tINVALID INPUT\n")        
            elif inp==2:
                year=getinput("Enter year: ","int")
                if year in yearlist:
                    q='select results_declared from election_status where election_type="pe"'
                    mb.execute(q)
                    f=mb.fetchone()
                    if f[0] in 'Yy':
                        winner(year,"AE")
                    else:
                        print("\n\t\t\tRESULTS NOT DECLARED\n")
                else:
                    print("\n\t\t\t\t\tINVALID INPUT\n")
        elif ch==4:
            print("\n\t\t\t1-Constituency Wise")
            print("\t\t\t2-Year wise")
            inp=getinput("Enter your choice(1/2): ","int")
            if inp==1:
                print("\t\t\t1-Parliamentary constituencies")
                print("\t\t\t2-Assembly constituencies")
                inp1=getinput("Enter your choice(1/2): ","int")
                if inp1==1:
                    year=getinput("Enter year: ","int")
                    if year in yearlist:
                        pcon=['North West Delhi','Chandini Chowk','West Delhi']
                        p=pe_candidate_vote(year)
                        print("_"*150)
                        print("\n%20s"%"Constituency","%40s"%"Vote received by candidates")
                        print("_"*150)
                        for i in range(len(pcon)):
                            print("%20s"%pcon[i])
                            for j in range(len(p[i])):
                                print("%40s"%p[i][j][0],"-",p[i][j][1])
                        print("-"*150)
                    else:
                        print("\n\t\t\t\t\tINVALID INPUT\n")
                elif inp1==2:
                    year=getinput("Enter year: ","int")
                    if year in yearlist:
                        acon=['Rohini', 'Rithala', 'Pitampura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Vikaspuri','Janakpuri','Shakur Basti']
                        a=ae_candidate_vote(year)
                        print("_"*150)
                        print("\n%25s"%"Constituency","%40s"%"Vote received by candidates")
                        print("_"*150)
                        for i in range(len(acon)):
                            print("%25s"%acon[i])
                            for j in range(len(a[i])):
                                print("%40s"%a[i][j][0],"-",a[i][j][1])
                            print("-"*150)
                    else:
                        print("\n\t\t\t\t\tINVALID INPUT\n")
                else:
                    print("\n\t\t\t\t\tINVALID INPUT\n")
            elif inp==2:
               y=year_candidate_vote()
               print("_"*150)
               print("\n%20s"%"Year","%40s"%"Votes received by candidates")
               print("_"*150)
               for i in range(len(yearlist)):
                   print("%20s"%yearlist[i])
                   for j in range(len(y[i])):
                       print("%40s"%y[i][j][0],"-",y[i][j][1])


        else:
            break
            
            #print("\n\t\t\tOPTION NOT IN MENU!!!!\n")
            
                
                        
                    
            

                

        
