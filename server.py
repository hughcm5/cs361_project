import csv


def print_column_headers(csv_file):
    """
    Print column headers for csv file 
    """
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)        
        headers = next(csv_reader)
        print(headers)

def create_parks_dictionary(csv_file):
    """
    Creates dictionary to store parks and fields in each zip code
    """
    parks_dict = {}


    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            zip_code = row['ZIP']
            park_name = row['PARK']
            num_baseball_fields = int(row['SUM'])

            if zip_code not in parks_dict:
                parks_dict[zip_code] = {'parks': [], 'fields': {}}

            if park_name not in parks_dict[zip_code]['parks']:
                parks_dict[zip_code]['fields'][park_name] = num_baseball_fields


    return parks_dict


csv_file_path = 'park_data.csv'
parks_dictionary = create_parks_dictionary(csv_file_path)


for zip_code, fields in parks_dictionary.items():
    print("ZIP Code: ", zip_code)
    #print("Park: ", data['parks'])
    print("Parks: ", fields['fields'])
    print()



