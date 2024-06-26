# importing necessary files 
import Display
import Rent
import datetime
import random
date = datetime.datetime.now()
currentDate = date.strftime("%m/%d/%Y")

# function for returners detail
def forReturnerName():
    global ReturnerName
    isreturn = True
    global returnNo
    returnNo=0
    print("\n!----------------- ENTER THE DETAILS OF RETURNER TO GENERATE BILL -----------------!\n")
    while (isreturn):
        ReturnerName = (
            # asks user for input 
            input("\n\t------- ENTER RETURNER NAME( WITHOUT SPACE) -------\n>>> ")).strip()
        # checks if the input is empty or not 
        if ReturnerName == "":
            print("\n!!!!!!! PLEASE INPUT RETURNERS NAME WITHOUT SPACE !!!!!!\n")
            isreturn = True
        # checks if the input is in alphabetical letter 
        elif ReturnerName.isalpha():
            returnNo = random.randint(1, 500)
            with open(ReturnerName+"_returnBills.txt", "w") as File:
                File.write("""
             +====================================== LILY RENTAL SHOP =====================================+
                 +==================================== RETURN BILL =====================================+
                  """)
                File.write(
                    f"Return No: {returnNo}\t\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                File.write(
                    f"\t\t\t\t\t\t\t Returner Name: {ReturnerName}\n\n")
                File.write(
                    "\t________________________________________________________________________________________\n\t")
                header = "{:<18} {:<15} {:<15} {:<15}{:}".format(
                         "NAME", "BRAND", "PRICE", "QUANTITY", "TOTAL")
                File.write(header + "\n")
                File.write(
            "========================================================================================\n")

                break
        else:
            print(
                "\n!!!!!!PLEASE INPUT RETURNERS NAME (ALPHABETICAL LETTERS )!!!!!!!\n")
            isreturn = True
    return isreturn

# function for calculation to generate reciept 
def ForReturnDetails(isreturn):
    inventory = Display.dictionaryObjects()
    Display.displayObjects()
    print("\n")
    global nettotal
    nettotal = 0
    global days
    days=0 
    global day1
    day1=0
    isreturned = False
    global Total 
    Total = 0 
    while isreturn:
        # try and except to handle exceptions thats likely to occur
        try:
            # asks users for input 
            print("\n\t----CHOOSE A ID NUMBER OF OBJECT FROM ABOVE LISTED TO RETURN-----\n")
            id = int(input("input "))
            if id in inventory.keys():
                loopReturn = True
                while loopReturn:
                    # try and except to handle exceptions thats likely to occur
                    try:
                        # asks user for input 
                        quantity = int(input("\n\t------------ ENTER THE QUANTITY OF THE OBJECT YOU WANT  TO RETURN ---------- \n\n input: "))
                        days= int(input("\n------ENTER THE NUMBER OF DAYS YOU RENTED IT FOR----\n\n input: "))
                        day1 = int(input("\n\t---------------- ENTER THE ACTUAL NUMBER OF DAYS YOU KEPT IT FOR ------------------\n\n input:  "))
                        # checks if given quantity is less than 0 or not 
                        if quantity <= 0:
                            print("!!!!!!!! PLEASE INPUT POSITIVE VALUE IN QUANTITY !!!!!!!")
                        # if not then calculates total amount 
                        else: 
                            loopReturn = False
                            isreturned = True
                            price = inventory[id]['PRICE'].replace("$", "")
                            actual_day= int(days)/5
                            Total = int(price) * int(actual_day)
                            nettotal = nettotal+ Total
                            with open(f"{ReturnerName}_returnBills.txt", "a+") as File:
                                File.write("{:<18} {:<15} {:<15} {:<15}{:}".format(inventory[id]['NAME'],
                                   inventory[id]['BRAND'], inventory[id]['PRICE'], quantity, nettotal))
                                File.write("\n\t")
                            # adding quantity after returning 
                            inventory[id]["QUANTITY"] += quantity
                    except ValueError:
                        print("\n!!!!!!! PLEASE ENTER INTEGER NUMBER !!!!!!!!")
                        loopReturn = True 
            else:
                print("\n------!!INVALID ID NUMBER. PLEASE CHECK YOUR GIVEN ID IN DISPLAY BOX CAREFULLY!!-------")
                isreturn= True
        except ValueError:
            print("\n!!!!!!! PLEASE ENTER INTEGER VALUE !!!!!!!!")
            isreturn= True
        while isreturned:
            print("\n\t---------  WOULD YOU LIKE TO RETURN MORE (y- yes / n- no )? --------\n")
            returnMore = input("input: ")
            # converts input values into lowercase and compares value 
            if returnMore.lower() == "y":
                isreturn = True
                loopReturn = True
                isreturned = False
            elif returnMore.lower() == "n":
                isreturn = False
                loopReturn = False
                isreturned = False
                Rent.writingObjects(inventory)
            else:
                print("\n!!!!!!! Please, Choose ('y' or 'n') !!!!!!!!!\n")

# function for return receipt 
def forReceiptGenerate():
    day2=days
    day3=day1
    grand_total= nettotal
    no= returnNo
    # checks if day2 is smaller than day3 or not 
    if (day2<=day3):
        # if yes then calcuates total with extra charge 
        extra_day= int(day3)-int(day2)
        extra_charge = extra_day * 30
        total_with_charge = extra_charge+ Total
      
        with open(f"{ReturnerName}_returnBills.txt", "a+") as File:
         File.write(
            f"""
             
            \n\t ________________________________________________________________________________________\n
                                                    TOTAL RENTED DAYS : {day2}\n
                                                    TOTAL RETURNED DAYS  : {day3}\n
                                                    EXTRA DAY :{extra_day}\n
                                                    TOTAL CHARGE WITHOUT EXTRA CHARGE :${grand_total}\n
                                                    EXTRA CHARGE :${extra_charge}\n
                 ___________________________________________________________________________________________\n
                                                     TOTAL AMOUNT TO PAY:${total_with_charge}\n
                  +========================================================================================+\n\n
                  
           +========================================THANKYOU FOR RETURNING ========================================+\n\t""")
         print("""
            !#######################!
            !                       !
            !  Return Successfully  !
            !                       !
            !#######################!""")
    else : 
        # if no then total amount with no charge is calculated 
        with open(f"{ReturnerName}_returnBills.txt", "w") as File:
         File.write(
            f"""
           
            \n\t________________________________________________________________________________________\n
                                                    TOTAL RENTED DAYS : {day2}\n
                                                    TOTAL RETURNED DAYS  : {day3}\n
                                                    EXTRA DAY : 0\n
                                                    TOTAL CHARGE WITHOUT EXTRA CHARGE :${grand_total}\n
                                                    EXTRA CHARGE :$ 0\n
                ___________________________________________________________________________________________\n
                                                     TOTAL AMOUNT TO PAY:${grand_total}\n
                  +========================================================================================+\n\n
                  
         +========================================THANKYOU FOR RETURNING ========================================+\n\t""")
         print("""
            !#######################!
            !                       !
            !  Return Successfully  !
            !                       !
            !#######################!""")
        