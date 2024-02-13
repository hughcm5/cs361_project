import csv

class Reservations:
    def __init__(self):
        self.reservations = {}

    def update_reservation(self, zip_code, reservation_info):
        self.reservations[zip_code] = reservation_info

    @staticmethod
    def read_reservations_from_file():
        filename = 'zip_codes.csv'
        column_index = 0

        reservations_instance = Reservations()

        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > column_index:
                    zip_code = row[column_index]
                    reservations_instance.update_reservation(zip_code, {})  # Initialize with default value
        return reservations_instance

    def get_reservations(self):
        return self.reservations





def main():
    header1 = print("BASEBALL FIELD RESERVATION SYSTEM")
    header2 = print("-------------------------------------------------")
    print("ENTER THE CHICAGO ZIP CODE YOU WOULD LIKE TO SEARCH")
    print("For information on Chicago zip codes type 'help' or, to quit, type 'stop'\n")
    reservations_instance = Reservations.read_reservations_from_file()

    zip_code = input("Enter ZIP code: ")
    if zip_code == 'stop':
        return
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
        main()
    elif zip_code not in reservations_instance.get_reservations():
        print("Invalid zip code")
        main()

if __name__ == '__main__':
    main()

    