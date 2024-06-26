
# Function For reading laptops from a file and storing it in a dictionary

def dictionaryObjects():
    objects = {}
    with open( 'data.txt', 'r') as storage:
        for line in storage:
            data = line.strip().split(",")
            print(data)
            id = len(objects) + 1
            objects[id] = {
                "NAME": data[0],
                "BRAND": data[1],
                "PRICE": data[2],
                "QUANTITY": int(data[3])
            }
    return objects

# Function for displaying stock laptops from stored dictionary


def displayObjects():
    objects = dictionaryObjects()
    print("\n#==================================== Available Stocks ===================================#")
    print("\n===========================================================================================")
    print("{:<8} {:<35} {:<20} {:<15} {:<25}".format("ID", "AVAILABLE OBJECTS",
                                                            "BRAND", "PRICE", "QUANTITY"))
    print("==============================================================================================\n")
    for id, data in objects.items():
        print("\033[35m{:<8}{:<35}{:<20}{:<15}{:<25}\033[0m".format(
            id, data['NAME'], data['BRAND'], data['PRICE'], data['QUANTITY']))
    print("\n#============================================================================================#")
   