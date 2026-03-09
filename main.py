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

        print(f"{'ID':<3} | {'TYPE':<10} | DATA")
        print("-" * 30)
        
        for i, shape in enumerate(shapes):
            shape_type = type(shape).__name__
            print(f"{i:<3} | {shape_type:<10} | {shape}")

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

    elif cmd == "help":
        print("""
Commands:
    create point x y
    create segment x1 y1 x2 y2
    create circle x y r
    create square x y size
    list          - show all shapes
    delete id     - delete shape by id
    help          - show this help
    exit          - exit program 
        """)

    else:
        print("Unknown command")