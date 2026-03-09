from shapes.point import Point

shapes = []

while True:
    command = input("> ")

    if command == "exit":
        break

    elif command == "list":
        for i, shape in enumerate(shapes):
            print(i, shape)

    elif command.startswith("create point"):
        parts = command.split()

        x = float(parts[2])
        y = float(parts[3])

        shapes.append(Point(x, y))
        print("Point created")

    else:
        print("Unknown command")