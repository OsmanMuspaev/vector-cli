shapes = []

while True:
    command = input("> ")

    if command == "exit":
        break

    elif command == "list":
        for i, shape in enumerate(shapes):
            print(i, shape)

    else:
        print("Unknown command")