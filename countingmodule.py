import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='12345$',database='voterdb')
mb=db.cursor()

def counting(n):
    q='select count(*) from voter_registration where age>={} and age<{}'.format(n,n+10)
    mb.execute(q)
    a=mb.fetchone()
    return (a[0])

def counting1(n):
    q='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.age>={} and voter_registration.age<{}'.format(n,n+10)
    mb.execute(q)
    a=mb.fetchone()
    return (a[0])
    
def counting2(n):
    q='select count(*) from voter_registration where '.format(n,n+10)
    mb.execute(q)
    a=mb.fetchone()
    return (a[0])

##def counting3():
##    parlcountlist=[]
##    parlconstlist=['North West Delhi','Chandi Chowk','West Delhi']
##    for i in parlconstlist:
##        q='select count(*) from voter_registration,voting_details where voter_registration.voter_id=voting_details.voter_id and voter_registration.parliamentary_constituency="{}"'.format(i)
##        mb.execute(q)
##        a=mb.fetchall()
##        parlcountlist.append(a[0][0])
##    return parlcountlist
    

    


