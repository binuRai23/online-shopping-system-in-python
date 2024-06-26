# importing necessary files 
import datetime
import random
import Display
date = datetime.datetime.now()
currentDate = date.strftime("%m/%d/%Y")

# function for getting data from txt file 
def writingObjects(objects):
    print(objects)
    with open("data.txt", "w") as d:
        for id, details in objects.items():
            if int(details['QUANTITY']) > 0:
                d.write(
                    f"{details['NAME']}, {details['BRAND']}, {details['PRICE']}, {details['QUANTITY']}\n")

# function for customername and receipt generation
def customer():
    global Name
    global isCreate
    isCreate = True
    print("\n!--- ENTER SOME DETAILS OF CUSTOMER TO GENERATE RECEIPT--- \n")
    while (isCreate):
        # asks user for input
        Name = (input("ENTER CUSTOMER NAME(without space): ")).strip()
       # checks if the input is empty or not 
        if Name == "":
            print("\n---- PLEASE ENTER THE CUSTOMER NAME WITHOUT SPACE----\n")
            isCreate = True
         # checks if the input is in alphabetical letter 
        elif Name.isalpha():
            rentNo = random.randint(1, 500)
            with open(Name+"_Rent_Receipt.txt", "w") as customerD:
                
                customerD.write("""
                     ================================= LILY RENTAL SHOP ====================================
                     ================================= RENT RECEIPT ========================================

        """)
                customerD.write(
                    f"Rent No: {rentNo}\t\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                customerD.write(
                    f"\t\t\t\t\t\t\tCustomer Name: {Name}\n\n")
                customerD.write(
                    "\t____________________________________________________________________________________________\n\t")
                customerD.write("{:<18} {:<15} {:<15} {:<15}{:}".format("NAME OF OBJECT",
                                                                           "BRAND", "PRICE", "QUANTITY", "TOTAL"))
                customerD.write(
                    "\n\t============================================================================================\n\t")
                break
        else:
            print(
                "\n---- PLEASE ENTER THE CUSTOMER NAME WITHOUT SPACE----\n")
            isCreate = True
    return isCreate



# function for calculation to generate reciept
def rentObjects(isCreate):
    inventory = Display.dictionaryObjects()
    Display.displayObjects()
    print("\n")
    global Grand_Total
    Grand_Total = 0
    global rent
    rent = False  
    global actual_day
    actual_day=0 
    global quantity 
    quantity =0 
    global amount 
    amount = 0 
    while isCreate:
         # try and except to handle exceptions thats likely to occur
        try:
            print(
                "\n\t-------CHOOSE A ID NUMBER OF OBJECT FROM ABOVE LISTED TO RENT-------\n")
            id = int(input("input: "))
            if id in inventory.keys():
                Rent1 = True
                while Rent1: 
                    # try and except to handle exceptions thats likely to occur
                    try:
                        # asks user for input 
                        quantity1 = int(inventory [id]['QUANTITY'])
                        print(f"\n QUANTITY AVAILABLE: {quantity1}")
                        quantity= int(input("\n\t------------ ENTER THE QUANTITY OF OBJECT TO RENT ----------\n\n input: "))
                        days =  int(input("\n For how many days do you want to rent? \n\n input: "))
                        # checks if given quantity is less than 0 or not 
                        if quantity <= 0:
                            Rent1 = True
                            print(
                                "\n!!!!!!!!PLEASE INPUT POSITIVE VALUE IN QUANTITY !!!!!!!")
                        # if not then calculates total amount   
                        elif inventory[id]["QUANTITY"] >= quantity:
                            Rent1 = False
                            rent = True
                            amount = int(inventory[id]['PRICE'].replace("$", ""))
                            actual_day= int(days)/5
                            Total = amount * actual_day
                            Grand_Total = Grand_Total + Total
                            with open(f"{Name}_Rent_Receipt.txt", "a+") as customer:
                                customer.write("{:<18} {:<15}{:<15} {:<15}{:}".format(
                                     inventory[id]['NAME'], inventory[id]['BRAND'], inventory[id]['PRICE'], quantity, Total))

                                customer.write("\n\t")
                            # substracting rented quantity
                            inventory[id]["QUANTITY"] -= quantity
                        else:
                            print(
                                "\n-------!!INSUFFICIENT QUANTITY OF SELECTED OBJECT!!-------\n")
                            Rent1 = True
                    except ValueError:
                        print(
                            "\n-------!!QUANTITY SHOULD BE IN INTEGER NUMBER!!-------\n")
                        Rent1 = True
            else:
                print(
                    "\n------!!INVALID ID NUMBER. PLEASE CHECK YOUR GIVEN ID IN DISPLAY BOX CAREFULLY!!-------\n")
                isCreate = True
        except ValueError:
            print("\n-------!!INVALID ID NUMBER. PLEASE INSERT INTEGER NUMBER FOR ID!!-------\n")
            isCreate = True
        while rent:
            print("\n\t------- WOULD YOU LIKE TO RENT MORE( y- yes/ n - no) ?-------- \n")
            rentMore = input("input: ")
             # converts input values into lowercase and compares value 
            if rentMore.lower() == "y":
                isCreate = True
                Rent1 = True
                rent = False
            elif rentMore.lower() == "n":
                isCreate = False
                rent = False
                writingObjects(inventory)
            else:
                print("\n-------!! PLEASE INSERT ('y' or 'n')!!-------\n")

# function for rent receipt 
def All():
    totalPrice = Grand_Total
    actualday= actual_day
    quan = quantity
    unit = amount
    print("""
        ------------------------------------------------------------------
        |        WOULD YOU LIKE TO RENT PHYSICALLY OR ONLINE?            |
        ------------------------------------------------------------------
        |                     1 FOR : PHYSICAL                           |
        |                     2 FOR : ONLINE                             |
        ------------------------------------------------------------------ """)
    while True:
         # try and except to handle exceptions thats likely to occur
        try:
            option = int(input("input: "))
            if option == 2:
                # adding shipping charge 
                ShippingPrice = totalPrice + 200
                with open(f"{Name}_Rent_Receipt.txt", "a+") as customer:
                   customer.write("""\n\t --------------------------------------------------------------------------------------------\n""")  
                   customer.write(
                          "                                                             TOTAL QUANTITY: "+str(quantity)+"\n")
                   customer.write("""\n\t --------------------------------------------------------------------------------------------\n""")  
                   customer.write(
                          "                                                             TOTAL DAYS(5 days=1 unit): "+str(actualday)+"\n")
                   customer.write(
                          "                                                            PRICE PER UNIT: "+str(unit)+"\n")
                   customer.write(
                          "                                                          TOTAL PRICE: $"+str(totalPrice)+"\n")
                   customer.write(
                          "                                                         SHIPPING CHARGE: $200\n ")
                   customer.write(
                         "                                                       TOTAL WITH SHIPPING CHARGE: $"+str(ShippingPrice))
                   customer.write("""\n\t--------------------------------------------------------------------------------------------\n""")
                   customer.write("""  ====================================THANKYOU FOR RENTING!!========================================""")
                print(""" 
                         +++++++++++++++++++++++++++++++++
                         +                               +
                         +    RENTED SUCCESSFULLY !!     +
                         +                               +
                         +++++++++++++++++++++++++++++++++ """) 
                return
            elif option == 1:
                with open(f"{Name}_Rent_Receipt.txt", "a+") as customer:
                    customer.write(
                        """\n\t----------------------------------------------------------------------------------------\n""")
                    customer.write(
                        "                                                TOTAL DAY (5 DAY = 1 UNIT):" + str(actualday)+"\n")
                    customer.write(
                        "                                                            PRICE PER UNIT : $" + str(amount)+"\n")
                    customer.write(
                        "                                                             TOTAL PRICE: "+str(totalPrice)+"\n")
                    
                    customer.write(
                        """---------------------------------------------------------------------------------------------\n""")
                    customer.write(
                        """ =====================================THANKYOU FOR RENTING!!===============================\n""")
                print(""" 
                         +++++++++++++++++++++++++++++++++
                         +                               +
                         +    RENTED SUCCESSFULLY !!     +
                         +                               +
                         +++++++++++++++++++++++++++++++++ """)   
                return
            else:
                print("\n\t-------!!PLEASE CHOOSE FROM GIVEN OPTIONS!!-------\n")
        except ValueError:
            print("\n-------!!PLEASE ENTER VALID OPTION OF INTEGER!!-------\n")
        totalPrice = 0

