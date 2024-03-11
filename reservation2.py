import zmq

def main():
    context = zmq.Context()

    print("Connecting to server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        # Take user input for the number
        zip_code = str(input("Zip code "))
        park = input("Park ")

        # Create a list with calorie count as a string and activity level as a string
        data = [zip_code, park]

        # Send the list to the server
        socket.send_json(data)

        # Receive and print the result
        result = socket.recv_string()
        print(f"Result: {result}")


if __name__ == "__main__":
    main()