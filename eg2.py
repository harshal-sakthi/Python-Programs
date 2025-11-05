with open("file_log.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if "ERROR".lower() in line:
            print(f"Found error: {line}")