import zmq
import csv
import time

def ascii_title():
    windycity = """
 _     _  ___   __    _  ______   __   __   _______  ___   _______  __   __                                 
| | _ | ||   | |  |  | ||      | |  | |  | |       ||   | |       ||  | |  |                                
| || || ||   | |   |_| ||  _    ||  |_|  | |       ||   | |_     _||  |_|  |                                
|       ||   | |       || | |   ||       | |       ||   |   |   |  |       |                                
|       ||   | |  _    || |_|   ||_     _| |      _||   |   |   |  |_     _|                                
|   _   ||   | | | |   ||       |  |   |   |     |_ |   |   |   |    |   |                                  
|__| |__||___| |_|  |__||______|   |___|   |_______||___|   |___|    |___|                                  
 ______    _______  _______  _______  ______    __   __  _______  _______  ___   _______  __    _  _______ 
|    _ |  |       ||       ||       ||    _ |  |  | |  ||   _   ||       ||   | |       ||  |  | ||       |
|   | ||  |    ___||  _____||    ___||   | ||  |  |_|  ||  |_|  ||_     _||   | |   _   ||   |_| ||  _____|
|   |_||_ |   |___ | |_____ |   |___ |   |_||_ |       ||       |  |   |  |   | |  | |  ||       || |_____ 
|    __  ||    ___||_____  ||    ___||    __  ||       ||       |  |   |  |   | |  |_|  ||  _    ||_____  |
|   |  | ||   |___  _____| ||   |___ |   |  | | |     | |   _   |  |   |  |   | |       || | |   | _____| |
|___|  |_||_______||_______||_______||___|  |_|  |___|  |__| |__|  |___|  |___| |_______||_|  |__||_______|                                             
        """
    return windycity

def display_header():
    """
    Display CLI headers
    """
    print(ascii_title())
    print("\nRESERVE A FIELD FOR FREE IN LESS THAN A MINUTE")
    print("-------------------------------------------------")
    print("For information on Chicago zip codes and information on the service type 'help' or, to quit, type 'stop' and hit enter\n")
    print("ENTER THE CHICAGO ZIP CODE YOU WOULD LIKE TO SEARCH")

def zip_code_reader():
    """
    Display zip codes availible and information on service
    """
    with open('zip_codes.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[0])

def help_menu():
    """
    Help menu responses
    """
    while True:
        print("Welcome to the WindyCity Reservations help menu! This service is designed to make reserving baseball diamonds in Chicago easier than ever!")
        print("To see all zip codes, type 'zip code', if you know a zip code and want to see the parks enter the zip code (ex. 60613)")
        print("To return to the reservation page, type 'back'\n")

        user = input("Enter: ")

        if user == 'zip code':
            zip_code_reader()
        elif user == 'back':
            main(connect_to_server())
            break
        else:
            search_parks_by_zip(user)
            
def search_parks_by_zip(zip_code):
    """
    Searches for parks by zip code provided by user
    """
    parks = []
    with open('park_data.csv', newline='') as file:
        reader = csv.reader(file)
        # iterate through csv file to find parks
        for row in reader:
            if len(row) >= 3 and row[1] == zip_code:
                parks.append(row[2])
    # print result if parks found
    if parks:
        print(f"Parks in ZIP code {zip_code}:")
        for park in parks:
            print(park)
    else:
        print(f"No parks found in ZIP code {zip_code}.")

def connect_to_server():
    """
    Make connection to microservice
    """
    # Connect to server
    context = zmq.Context()
    print("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    time.sleep(1.0)
    print("Connected to server")
    return socket

def main(socket):
    """
    Main method that takes user input and calls all other methods
    """
    while True:
        # Display header and information
        display_header()

        # Take user input
        zip_code = input("Enter ZIP code: ")
        park = input("Enter Park: ")

        # Check for help or stop
        if zip_code.lower() == 'help' or park.lower() == 'help':
            help_menu()
            continue

        # End program if 'stop'
        if zip_code.lower() == 'stop' or park.lower() == 'stop':
            return

        print("Getting ready to send information to server...")
        back = (input("Continue(Y/N): "))
        time.sleep(1.0)

        if back.lower() != 'n':
            # Create a list of zip code and park data
            data = [zip_code, park]
            # Send the list to the server
            socket.send_json(data)
        else:
            # Start over
            main(connect_to_server())

        # Receive and print the result
        result = socket.recv_string()
        print(f"Result: {result}")
        time.sleep(1.0)

if __name__ == "__main__":
    socket = connect_to_server()
    main(socket)