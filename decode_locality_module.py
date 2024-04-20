def decode_locality():
        print("Tell us where you reside. Choose one of the following.\n\n\n")
        print("Rohini : 1\nRithala : 2\nPitamPura/Shalimar Bagh: 3\nBawana : 4\nBurari: 5\nMangol Puri : 6\nBadli : 7\nVikaspuri : 8\nJanakpuri : 9\nShakur Basti : 10")
        ch=int(input("\n\nEnter Locality : "))
        while True:
            if ch==1:
                  locality='Rohini'
                  Assembly_constituency='Rohini'
                  Parliamentary_constituency='North West Delhi'
                  break
            elif ch==2:
                  locality='Rithala'
                  Assembly_constituency='Rithala'
                  Parliamentary_constituency='North West Delhi'
                  break
            elif ch==3:
                  locality='Shalimar Bagh'
                  Assembly_constituency='Shalimar Bagh'
                  Parliamentary_constituency='Chandni Chowk'
                  break
            elif ch==4:
                  locality='Bawana'
                  Assembly_constituency='Bawana'
                  Parliamentary_constituency='North West Delhi'
                  break
            elif ch==5:
                  locality='Burari'
                  Assembly_constituency='Burari'
                  Parliamentary_constituency='North East Delhi'
                  break
            elif ch==6:
                  locality='Mangol Puri'
                  Assembly_constituency='Mangol Puri'
                  Parliamentary_constituency='North West Delhi'
                  break
            elif ch==7:
                  locality='Badli'
                  Assembly_constituency='Badli'
                  Parliamentary_constituency='North West Delhi'
                  break
            elif ch==8:
                  locality='Vikaspuri'
                  Assembly_constituency='Vikaspuri'
                  Parliamentary_constituency='West Delhi'
                  break
            elif ch==9:
                  locality='Janakpuri'
                  Assembly_constituency='Janakpuri'
                  Parliamentary_constituency='West Delhi'
                  break
            elif ch==10:
                  locality='Shakur Basti'
                  Assembly_constituency='Shakur Basti'
                  Parliamentary_constituency='Chandni Chowk'
                  break
            else:
                print('Invalid input..try again')
        return locality,Assembly_constituency,Parliamentary_constituency
