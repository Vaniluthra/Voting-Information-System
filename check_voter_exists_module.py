import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', password='12345$', database='voterdb')
mb=db.cursor()

def check_voter_exists(voterid,table):
    try:
        if table=='NV':
            q1="select count(Voter_ID) from Voter_Registration where Voter_ID='{}'".format(voterid)
            mb.execute(q1)
            check=mb.fetchone()
        elif table=='NC':
            q1="select count(Voter_ID) from Candidate_Registration where Voter_ID='{}'".format(voterid)
            mb.execute(q1)
            check=mb.fetchone()

    except mysql.connector.Error as error:
            print("Failed to verify if Voter exists {}".format(error))        

    return check[0]
