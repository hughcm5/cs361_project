import csv

def main():
    header1 = print("\nBASEBALL FIELD RESERVATION SYSTEM -- RESERVE A FIELD IN LESS THAN A MINUTE")
    header2 = print("-------------------------------------------------")
    print("ENTER THE CHICAGO ZIP CODE YOU WOULD LIKE TO SEARCH")
    print("For information on Chicago zip codes type 'help' or, to quit, type 'stop'\n")

    reservations_instance = Reservations.read_reservations_from_file()

    zip_code = input("Enter ZIP code: \n")

    # STOP PROGRAM
    if zip_code == 'stop':
        return
    
    # SHOW USER ZIP CODES  
    elif zip_code == 'help':
        csv_zipcodes = 'zip_codes.csv'
        column_index = 0
        print(header1)
        print(header2)

        with open(csv_zipcodes, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > column_index:
                    print(row[column_index])
        main()   # Prompts user again

    if zip_code in reservations_instance.get_reservations():
        print("\n To start over type 'back'.\n")
        name = input("What is the name for the reservation? ")
        if name != 'back':   # Backtrack 
            park = input("Which park would you like to reserve? ")
            if park == 'back':
                main()
        if name == 'back':
            main()

        reservation_info = [name, park] # Create list for inputs

        # Add park to Zip Code
        reservations_instance.update_reservation(zip_code, reservation_info)
        #print(reservations_instance.get_reservation_info(zip_code))

        print("Okay, " + name + ", you would like to reserve a field " + park + " Chicago, IL " + zip_code)
        choice = input("Is this correct? (Y/N) ")
        
        # USER CONFIRM RESERVATION
        choice
        if choice == 'Y':
            print("Field reserved!")
        if choice == 'N':
            print("Reservation canceled")
            main()
        

    
    else:
        print("Invalid zip code")
        main()

if __name__ == '__main__':
    main()

    reservation_instance = Reservations.read_reservations_from_file()

    print(reservation_instance.get_reservations())

    