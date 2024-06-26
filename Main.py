# importing neccessary files 
import os
import Rent
import Return
import Display

# creating user function to call other functions in imported files 
def user():
    print ("""\n ---------------------------- WELCOME TO LILY RENTAL SHOP ------------------------\n""")
    while (True):
        print("""\n
                             -----------------------------------------
                             !           LILY RENTAL SHOP            !
                             -----------------------------------------
                             !      1: Display available things      !   
                             !      2: Rent available things         !   
                             !      3: Return rented things          !
                             !      4: exit shop                     !  
                             -----------------------------------------    
             """)
        # try and except to handle exceptions thats likely to occur 
        try:
            # asks user for input 
            Input = int(input(" Enter a option to procced: >> "))
            # checks the input value and displays according to it 
            if Input == 1:
                Display.displayObjects()

            elif Input == 2:
                isGenerate = Rent.customer()
                Rent.rentObjects(isGenerate)
                Rent.All()
                print("""-------------------------""")
                print("""|  PLEASE, VISIT AGAIN  |""")
                print("""-------------------------""")
                os.startfile(f"{Rent.Name}_Rent_Receipt.txt")
            
            elif Input == 3:
                isCreate = Return.forReturnerName()
                Return.ForReturnDetails(isCreate)
                Return.forReceiptGenerate()
                os.startfile(f"{Return.ReturnerName}_returnBills.txt")

            elif Input == 4:
                print("\n**********!!!!!! PLEASE VISIT US AGAIN !!!!!!*********\n")
                break
            else:
                print("\n!!------- PLEASE CHOOSE FROM ABOVE GIVEN OPTIONS --------!!")

        except ValueError:
            print("\n!!-------- PLEASE INPUT A VALID OPTION NUMBER -------!!")

user()
