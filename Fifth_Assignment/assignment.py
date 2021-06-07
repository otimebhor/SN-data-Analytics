filename = "myfile.txt"

with open(filename, "w") as f:
    f.write("2x1 = 2 \n2x2 = 4\n2x3 = 6\n2x4 = 8\n2x5 = 10\n2x6 = 12\n2x7 = 14\n2x8 = 16\n2x9 = 18\n2x10 = 20\n2x11 = 11\n2x12 = 24")
with open(filename, "r") as f:
    print(f.read())