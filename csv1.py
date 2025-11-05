with open("file.csv", "r") as infile, open("outfile.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)
