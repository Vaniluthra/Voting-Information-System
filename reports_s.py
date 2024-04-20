def mainfunction1():
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='root',password='12345$',database='voterdb')
    mb=db.cursor()

    #functions
    #F0 - -MENU
    #with change1




    def menu():
        print("\n")
        print("*"*70)
        print("\n\t\t\tVOTER INFORMATION MENU\n")
        print("\nA. Number of registered voters ")
        print("\nB. Voter Turn-out in Parliamentary elections")
        print("\nC. Voter Turn-out in Assembly elections")
        print("\nD. Go back to Reports Menu\n")
        print("*"*70)

    #F1-counting voters agewise

    #F1.1 - totalvoters

    def totalcount():                ###################################################
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        totalcountlist=[]
        from countingmodule import counting
        for i in range(18,89,10):
            totalcountlist.append(counting(i))
        q1='select count(*) from Voter_Registration where age>=98'
        mb.execute(q1)
        a=mb.fetchone()
        totalcountlist.append(a[0])
        return (totalcountlist)

    #F1.2 - people who voted

    def actualcount():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        votercountlist=[]
        from countingmodule import counting1
        for i in range(18,89,10):
            votercountlist.append(counting1(i))
        q1='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.age>98'
        mb.execute(q1)
        a=mb.fetchone()
        votercountlist.append(a[0])
        return (votercountlist)

    def ageturnout():
        t=totalcount()
        a=actualcount()
        ageturnoutlist=[]
        for i in range(9):
            if t[i]!=0:
                ageturnoutlist.append((a[i]/t[i])*100)
            else:
                ageturnoutlist.append("No registered voter ")   #as division by 0 will give error
                
        return ageturnoutlist
            
            

    #F2-counting male and female voters

    #F2.1- malecount

    def malecount():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()

        #total
        
        q='select count(*) from voter_registration where gender="m"'
        mb.execute(q)
        mtotal=mb.fetchone()

        #actual

        q1='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.gender="m"'
        mb.execute(q1)
        mvoted=mb.fetchone()

        return [mtotal,mvoted]

    #F2.2-femalecount

    def femalecount():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()

        #total
        
        q='select count(*) from voter_registration where gender="f"'
        mb.execute(q)
        ftotal=mb.fetchone()
        

        #actual

        q1='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.gender="f"'
        mb.execute(q1)
        fvoted=mb.fetchone()

        return [ftotal,fvoted]

    def genderturnout():
        mtotal=m[0][0]
        mvoted=m[1][0]
        ftotal=f[0][0]
        fvoted=f[1][0]
        turnoutlist=[]
        if mtotal!=0:
            turnoutlist.append('No registered voter')
        else:
            turnoutlist.append(mtotal/mvoted)
        if ftotal!=0:
            turnoutlist.append('No registered voter')
        else:
            turnoutlist.append(ftotal/fvoted)
        
        return turnoutlist


    #F3- counting voters election wise

    #F3.1 - parliamentary

    #total

    def parliamentarycount():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        total_p_list=[]
        parlconstlist=['North West Delhi','Chandi Chowk','West Delhi']
        for i in parlconstlist:
            q="select count(*) from voter_registration where parliamentary_constituency='{}'".format(i)
            mb.execute(q)
            a=mb.fetchone()
            total_p_list.append(a[0])
        return total_p_list

    #voted

    def pvoted():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        parlcountlist=[]
        parlconstlist=['North West Delhi','Chandi Chowk','West Delhi']
        for i in parlconstlist:
            q='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.parliamentary_constituency="{}"'.format(i)
            mb.execute(q)
            a=mb.fetchall()
            parlcountlist.append(a[0][0])
        return parlcountlist

    #pturnout
    def pturnout():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        c=parliamentarycount()
        v=pvoted()
        pturnoutlist=[]
        for i in range(3):
            if c[i]!=0:
                pturnoutlist.append((v[i]/c[i])*100)
            else:
                pturnoutlist.append('No registered voter')
                
        return pturnoutlist
            
        
        

    #F3.2 - assembly

    #total

    def assemblycount():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        
        total_a_list=[]
        assemblyconstlist=['Rohini','Rithala','PitamPura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Badli','Vikaspuri','Janakpuri','Shakur Basti']
        for i in assemblyconstlist:
            q="select count(*) from voter_registration where assembly_constituency='{}'".format(i)
            mb.execute(q)
            a=mb.fetchone()
            total_a_list.append(a[0])
        return total_a_list

    #voted

    def avoted():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        acountlist=[]
        aconstlist=['Rohini','Rithala','PitamPura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Badli','Vikaspuri','Janakpuri','Shakur Basti']
        for i in aconstlist:
            q='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.assembly_constituency="{}"'.format(i)
            mb.execute(q)
            a=mb.fetchall()
            acountlist.append(a[0][0])
        return acountlist




    #aturnout

    def aturnout():
        import mysql.connector
        db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
        mb=db.cursor()
        c=assemblycount()
        v=avoted()
        aturnoutlist=[]
        for i in range(10):
            if c[i]!=0:
                aturnoutlist.append((v[i]/c[i])*100)
            else:
                aturnoutlist.append('No registered voter')
                
        return aturnoutlist



    ##################################              PRINTING               #################################################################

    while True:
        menu()
        inp=input("\nEnter your choice ")

        if inp in('Aa'):
            print("\n1. Age wise ")
            print("\n2. Gender wise ")
            print("\n3. Constituency wise ")
        
            inp1=int(input("\nEnter your choice "))

            if inp1==1:
                totalcountlist=totalcount()
            
                agegrouplist=['18-28','28-38','38-48','48-58','58-68','68-78','78-88','88-98','>98']
                print("_"*70)
                print("\n%20s"%"Age Group","%50s"%"Total number of registered voters")
                print("_"*70)
                for i in range(9):
                    print("%10s"%agegrouplist[i],"%50s"%totalcountlist[i])
                print("_"*70)
            elif inp1==2:
                m=malecount()
                mtotal=m[0][0]
                f=femalecount()
                ftotal=f[0][0]
                print("_"*70)
                print("\n%10s"%"Gender","%50s"%"Total number of registered voters")
                print("_"*70)
                print("%10s"%'Male',"%50s"%mtotal)
                print("%10s"%'Female',"%50s"%ftotal)
                print("_"*70)
                
            elif inp1==3:
                print("\na - Parliamentary Constituency ")
                print("\nb - Assembly Constituency ")
                inp2=input("\nEnter your choice ")


                if inp2=='a' or inp2=='A':
                    total_p_list=parliamentarycount()
                    parlconstlist=['North West Delhi','Chandi Chowk','West Delhi']
                    print("_"*72)
                    print("\n%20s"%"Constituency","%50s"%"Total number of eligible voters")
                    print("_"*72)
                    for i in range(3):
                        print("%20s"%parlconstlist[i],"%50s"%total_p_list[i])
                    print("_"*72)
                    
                elif inp2=='b' or inp2=='B':
                    total_a_list=assemblycount()
                    assemblyconstlist=['Rohini','Rithala','PitamPura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Badli','Vikaspuri','Janakpuri','Shakur Basti']
                    print("_"*70)
                    print("\n%50s"%"Constituency","%50s"%"Total number of eligible voters")
                    print("_"*70)
                    for i in range(10):
                        print("%50s"%assemblyconstlist[i],"%50s"%total_a_list[i])
                    print("_"*70)
                else:
                    print("\n\n\t\t\tEnter valid choice\n\n ")


        elif inp in('Bb'):
            import mysql.connector
            db=mysql.connector.connect(host='localhost',user='root',password='mysql',database='voterdb')
            mb=db.cursor()
            q='select results_declared from election_status where election_type="pe"'
            mb.execute(q)
            a=mb.fetchone()
            if a[0] in ('Yy'):
                print("\n1. Age wise ")
                print("\n2. Gender wise (Male-Female Ratio) ")
                print("\n3. Constituency wise ")

                inp1=int(input("\n\nEnter your choice "))

                if inp1==1:
                    totalcountlist=totalcount() ################################################
                    
                    votercountlist=actualcount()
                    ageturnoutlist=ageturnout()
                    agegrouplist=['18-28','28-38','38-48','48-58','58-68','68-78','78-88','88-98','>98']
                    print("_"*120)
                    print("\n%10s"%"Age Group","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%20s"%"Turn-out")
                    print("_"*120)
                    for i in range(9):
                        print("%10s"%agegrouplist[i],"%35s"%totalcountlist[i],"%35s"%votercountlist[i],"%30s"%ageturnoutlist[i])
                    print("_"*120)
                    
                elif inp1==2:
                    #total male count
                    m=malecount()
                    mtotal=m[0][0]
                    #male who voted
                    m=femalecount()
                    mvoted=m[1][0]

                    #total female count
                    f=femalecount()
                    ftotal=f[0][0]

                    #female who voted
                    f=femalecount()
                    fvoted=f[1][0]

                    #printing turnout
                    turnoutlist=genderturnout()
                    if turnoutlist[0]=='No registered voter':
                        print("\nNo registered male voter")
                    elif turnoutlist[1]=='No registered voter':
                        print("\nNo registered female voter")
                    else:
                        
                        print("_"*70)
                        print("\n%10s"%"Gender","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%30s"%"Turn-out")
                        print("_"*70)
                        print("%10s"%'Male',"%35s"%mtotal,"%35s"%mvoted,"%30s"%turnoutlist[0])
                        print("%10s"%'Female',"%35s"%ftotal,"%35s"%fvoted,"%30s"%turnoutlist[1])
                        print("\t\t\t\tMale : Female Ratio :",(int(turnoutlist[0])/int(turnoutlist[1])))
                        print("_"*70)




                elif inp1==3:
                    parlconstlist=['North West Delhi','Chandi Chowk','West Delhi']
                    total_p_list=parliamentarycount()
                    voted_p_list=pvoted()
                    pturnoutlist=pturnout()
                
                    print("_"*134)
                    print("\n%25s"%"Constituency","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%30s"%"Turn-out")
                    print("_"*134)
                    for i in range(3):
                        print("%25s"%parlconstlist[i],"%35s"%total_p_list[i],"%35s"%voted_p_list[i],"%30s"%pturnoutlist[i])
                    print("_"*134)
            else:
                print("\n\n\t\t\t\t\t\t****Result not declared**** ")


        elif inp in('Cc'):
            q='select results_declared from election_status where election_type="ae"'
            mb.execute(q)
            a=mb.fetchone()
            
            if a==None: 
                print("\n\n\t\t\t\t\t\t****Result not declared**** ")
            elif a[0] in ('Yy'): 
                print("\n1. Age wise ")
                print("\n2. Gender wise (Male-Female Ratio) ")
                print("\n3. Constituency wise ")

                inp1=int(input("\n\nEnter your choice "))
                if inp1==1:
                    totalcountlist=totalcount()
                    votercountlist=actualcount()
                    ageturnoutlist=ageturnout()
                    agegrouplist=['18-28','28-38','38-48','48-58','58-68','68-78','78-88','88-98','>98']
                    print("_"*70)
                    print("\n%10s"%"Age Group","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%20s"%"Turn-out")
                    print("_"*70)
                    for i in range(9):
                        print("%10s"%agegrouplist[i],"%35s"%totalcountlist[i],"%35s"%votercountlist[i],"%30s"%ageturnoutlist[i])
                    print("_"*70)
                    
                elif inp1==2:
                    #total male count
                    m=malecount()
                    mtotal=m[0][0]
                    #male who voted
                    m=femalecount()
                    mvoted=m[1][0]

                    #total female count
                    f=femalecount()
                    ftotal=f[0][0]

                    #female who voted
                    f=femalecount()
                    fvoted=f[1][0]



                    #printing turnout
                    turnoutlist=genderturnout()
                    if turnoutlist[0]=='No registered voter':
                        print("\nNo registered male voter")
                    elif turnoutlist[1]=='No registered voter':
                        print("\nNo registered female voter")
                    else:
                        
                        print("_"*70)
                        print("\n%10s"%"Gender","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%30s"%"Turn-out")
                        print("_"*70)
                        print("%10s"%'Male',"%35s"%mtotal,"%35s"%mvoted,"%30s"%turnoutlist[0])
                        print("%10s"%'Female',"%35s"%ftotal,"%35s"%fvoted,"%30s"%turnoutlist[1])
                        print("\t\t\t\tMale : Female Ratio :",(int(turnoutlist[0])/int(turnoutlist[1])))
                        print("_"*70)
                    

                elif inp1==3:
                    aconstlist=['Rohini','Rithala','PitamPura/Shalimar Bagh','Bawana','Burari','Mangol Puri','Badli','Vikaspuri','Janakpuri','Shakur Basti']
                    total_a_list=assemblycount()
                    voted_a_list=avoted()
                    aturnoutlist=aturnout()

                    print("_"*70)
                    print("\n%25s"%"Constituency","%35s"%"Total number of registered voters","%35s"%"Number of people who voted","%30s"%"Turn-out")
                    print("_"*70)
                    for i in range(10):
                        print("%25s"%aconstlist[i],"%35s"%total_a_list[i],"%35s"%voted_a_list[i],"%30s"%aturnoutlist[i])
                    print("_"*70)
        


        else:
            break



