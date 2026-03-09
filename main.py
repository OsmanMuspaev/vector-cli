from factory import ShapeFactory

shapes = []

while True:
    command = input("> ").strip()
    parts = command.split()

    if not parts:
        continue

    cmd = parts[0]

    if cmd == "exit":
        break

    elif cmd == "list":

        if not shapes:
            print("No shapes created")
            continue

        for i, shape in enumerate(shapes):
            print(f"{i}: {shape}")

    elif cmd == "create":

        try:
            shape = ShapeFactory.create(parts)
            shapes.append(shape)
            print("Shape created")

        except Exception as e:
            print("Error:", e)

    elif cmd == "delete":

        try:
            idx = int(parts[1])

            if idx < 0 or idx >= len(shapes):
                print("Invalid id")
            else:
                shapes.pop(idx)
                print("Shape deleted")
        
        except:
            print("Invalid command")
    else:
        print("Unknown command")