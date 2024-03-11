import zmq
import csv

class Storage:
    def __init__(self) -> None:
        self.parks_dict = {}

    def get_park_dict(self):
        """
        Gets dictionary info
        """
        return self.parks_dict
    
    def set_park_dict(self, parks_dict):
        """
        Sets parks dictionary
        """
        self.parks_dict = parks_dict

    def create_parks_dictionary(self):
        """
        Creates dictionary to store parks and fields in each zip code
        """
        # Initialize or clear the parks dictionary
        self.parks_dict = {}

        with open('park_data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                zip_code = row['ZIP']
                park_name = row['PARK']
                num_baseball_fields = int(row['SUM'])

                if zip_code not in self.parks_dict:
                    self.parks_dict[zip_code] = {'fields': {}}

                if park_name not in self.parks_dict[zip_code]['fields']:
                    self.parks_dict[zip_code]['fields'][park_name] = num_baseball_fields


class Reservations:

    def __init__(self) -> None:
        self._valid = True


    def make_reservation(self, zip_code, park):
        """
        Searches for park by zip code and park name.

        Decrements field amount if zip code and park are valid 
        """
        storage = Storage()

        storage.create_parks_dictionary()

        park_data = storage.get_park_dict()
        print("Park data:", park_data)

        # Check if the zip code exists in the park data
        if zip_code in park_data:
            print("Zip code found:", zip_code)
            parks_dict = park_data[zip_code].get('fields', {})
            # Check if the park name exists in the parks dictionary for the given zip code
            if park in parks_dict:
                print("Park found:", park)
                # Decrement the field amount for the park by 1
                parks_dict[park] -= 1
                print("Reservation made for", park)
                self._valid = True
            else:
                print("Park not found in zip code:", zip_code)
                self._valid = False
        else:
            print("Zip code not found:", zip_code)
            self._valid = False
        

    def get_valid(self):
        return self._valid



def main():
    
    context = zmq.Context()

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  

    print("Server running") # Check if server is running

    while True:
        reservations = Reservations()
        storage = Storage()


        # Receive data from client
        data = socket.recv_json()
        

        # Get first and second items of list
        zip_code = data[0]
        print(zip_code)
        park = data[1]
        print(park)

        reservations.make_reservation(zip_code,park)

        if reservations.get_valid() is True:
            result_str = "Reservation Successful!"
            storage.create_parks_dictionary()
            print(storage.get_park_dict())
        else:
            result_str = "Reservation Unsuccessful."


        # Send back to client
        # Maybe enclose this with if statement checking to see if reservation was sucessful
        # True/False
        socket.send_string(result_str)

if __name__ == "__main__":
    main()

