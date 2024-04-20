def Get_AE_PE_Name(ae_pe):
    if ae_pe=='A':
        print("Choose one of the following.")
        print("Rohini : 1\nRithala : 2\nPitamPura/Shalimar Bagh: 3\nBawana : 4\nBurari: 5\nMangol Puri : 6\nBadli : 7\nVikaspuri : 8\nJanakpuri : 9\nShakur Basti : 10")
        ch=int(input("Enter AE Contesting Constituency : "))
        while True:
            if ch==1:
                  constituency='Rohini'
                  break
            elif ch==2:
                  constituency='Rithala'
                  break
            elif ch==3:
                  constituency='Shalimar Bagh'
                  break
            elif ch==4:
                  constituency='Bawana'
                  break
            elif ch==5:
                  constituency='Burari'
                  break
            elif ch==6:
                  constituency='Mangol Puri'
                  break
            elif ch==7:
                  constituency='Badli'
                  break
            elif ch==8:
                  constituency='Vikaspuri'
                  break
            elif ch==9:
                  constituency='Janakpuri'
                  break
            elif ch==10:
                  constituency='Shakur Basti'
                  break
            else:
                print('Invalid input..try again')
                
    else:
        print("Choose one of the following : ")
        print("North West Delhi : 1\tChandni Chowk : 2\tWest Delhi : 3")
        ch=int(input("Enter PE Contesting Constituency : "))
        while True:
            if ch==1:
                  constituency='North West Delhi'
                  break
            elif ch==2:
                  constituency='Chandni Chowk'
                  break
            elif ch==3:
                  constituency='West Delhi'
                  break
            else:
                print('Invalid input..try again')
                
    return constituency

