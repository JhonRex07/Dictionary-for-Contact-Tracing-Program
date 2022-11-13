# Write a Python Program for Contact Tracing Using Dictionaries
print(">>>>>> DATA STRUCTURES AND ALGORITHMS <<<<<<")
print(">>>>>> CONTACT TRACING <<<<<<\n")

# Display Menu Options
def menu():
    print("=========== MENU: ============")
    print("=== 1 --> ADD AN ITEM      ===")
    print("=== 2 --> SEARCH           ===")
    print("=== 3 --> EXIT (y/n)       ===")
    print("==============================")
    
# Variables and Menu Options
menu()
dictionary = {
    "Full Name": " ",
    "Age": " ",
    "Address": " ",
    "Phone Number": " ",
}
number_list = []
numbers = 0

while True:
    options = int(input("\nWhat do you want to do (1/2/3): "))

# Adding an Item
    if options == 1:
        print("\nYou've chosen to ADD AN ITEM!")
        full_name = input("Enter the Full Name: ")
        dictionary["Full Name"] = full_name
        
        age = input("Enter the Age: ")
        dictionary["Age"] = age
        
        address = input("Enter the Address: ")
        dictionary["Address"] = address
        
        phone_number = input("Enter the Phone Number: ")
        dictionary["Phone Number"] = phone_number
        
        print("\n>>>>>>>>>> RESULTS <<<<<<<<<<")
        print(dictionary)
        
        numbers = numbers + 1
        number_list.append(numbers)
        print("YOU HAVE SUCCESSFULLY ADDED THIS ITEM!", numbers, "NEW ITEM ADDED\n")
        menu()

# Searching
    elif options == 2:
        print("\nYou've chosen to SEARCH AN ITEM!")
        print("=========== SEARCH ===========")
        print("===== A - FULL NAME      =====")
        print("===== B - AGE            =====")
        print("===== C - ADDRESS        =====")
        print("===== D - PHONE NUMBER   =====")
        print("==============================")
        
        search = str(input("\nPlease enter your choice (A/B/C/D): "))
        if search == "A":
            full_name = input("Enter the FULL NAME: ")
            dictionary["Full Name"] = full_name
            print(dictionary)
        
        elif search == "B":
            age = input("Enter the AGE: ")
            dictionary["Age"] = age
            print(dictionary)
        
        elif search == "C":
            address = input("Enter the ADDRESS: ")
            dictionary["Address"] = address
            print(dictionary)
            
        elif search == "D":
            phone_number = input("Enter the PHONE NUMBER: ")
            dictionary["Phone Number"] = phone_number
            print(dictionary)
        
# Exiting the Program

    elif options == 3:
        choose = input("Do you want to exit the program? (y/n) ")
        if choose == "y":
            exit()
        else:
            menu()
            continue
    else:
        print("INVALID OPTION! NOT IN THE MENU")



