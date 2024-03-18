import zmq
import csv
import time

def ascii_title():
    windycity = """
     _    _ _           _       _____ _ _          ______ _____ _____ 
    | |  | (_)         | |     /  __ (_) |         | ___ \  ___/  ___|
    | |  | |_ _ __   __| |_   _| /  \/_| |_ _   _  | |_/ / |__ \ `--. 
    | |/\| | | '_ \ / _` | | | | |   | | __| | | | |    /|  __| `--. \
    \  /\  / | | | | (_| | |_| | \__/\ | |_| |_| | | |\ \| |___/\__/ /
     \/  \/|_|_| |_|\__,_|\__, |\____/_|\__|\__, | \_| \_\____/\____/ 
                           __/ |             __/ |                    
                          |___/             |___/ 
        """
    return windycity

def display_header():
    """
    Display CLI headers
    """
    ascii_title()
    print("\nRESERVE A FIELD FOR FREE IN LESS THAN A MINUTE")
    print("-------------------------------------------------")
    print("For information on Chicago zip codes and information on the service type 'help' or, to quit, type 'stop' and hit enter\n")
    print("ENTER THE CHICAGO ZIP CODE YOU WOULD LIKE TO SEARCH")

def zip_code_reader():
    """
    Display zip codes availible and information on service
    """
    print("Welcome to WindyCity Reservations! This service is designed to make reserving baseball diamonds in Chicago easier than ever!")
    print("Enter the zip code and the park name below to reserve a field")

    with open('zip_codes.csv', 'r') as file:
        csv_reader = csv.reader(file)

        # Iterate over reach row in the second column
        for row in csv_reader:
            print(row[0])

def connect_to_server():
    """
    Make connection to microservice
    """
    # Connect to server
    context = zmq.Context()
    print("Connecting to server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
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
        if zip_code == 'help' or park == 'help':
            zip_code_reader()
            continue

        # End program if 'stop'
        if zip_code == 'stop' or park == 'stop':
            return

        print("Getting ready to send information to server...")
        back = (input("Continue(Y/N): "))
        time.sleep(1.0)

        if back != 'N':
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