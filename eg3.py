with open("file_log.txt", "r") as file:
    for _ in range(16):
        print(file.readline().strip())