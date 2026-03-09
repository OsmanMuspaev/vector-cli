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

    elif cmd == "update":
        try:
            idx = int(parts[1])
            if idx < 0 or idx >= len(shapes):
                print("Invalid id")
                continue

            shape = shapes[idx]
            shape.update(parts[2:])
            print("Shape updated")

        except Exception as e:
            print("Error:", e)

    elif cmd == "clear":
        shapes.clear()
        print("All shapes deleted")
    
    elif cmd == "info":
        try:
            idx = int(parts[1])
            shape = shapes[idx]
            print(f"ID {idx}: {type(shape).__name__} -> {shape}")
        except:
            print("Invalid id")

    elif cmd == "help":
        print("""
Commands:
              
  create <shape> <parameters>
    - point x y           : create a Point
    - segment x1 y1 x2 y2 : create a Segment
    - circle x y r        : create a Circle
    - square x y size     : create a Square
              
  list
    - show all created shapes in a table with ID, TYPE and DATA
              
  update <id> <parameters>
    - modify a shape by its ID
      Point: update <id> x y
      Segment: update <id> x1 y1 x2 y2
      Circle: update <id> x y r
      Square: update <id> x y size
              
  delete <id>
    - remove a shape by its ID

  clear
    - delete all shapes from the editor
                   
  info <id>
    - show detailed information about a shape
              
  help
    - show this help message

  exit
    - exit the program
        """)

    else:
        print("Unknown command, type 'help'")