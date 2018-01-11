# Charles Buyas cjb8qf


# neighbors = ["Jason", "Tristan", "Boyan", "Logan", "Taylor"]
outfile = open("neighbors.txt", "w")
outfile.write("Jason\n")
outfile.write("Tristan\n")
outfile.write("Boyan\n")
outfile.write("Logan\n")
outfile.write("Taylor\n")

outfile = open("neighbors.txt", "a")
for count in range(2):
    name = input("Please enter a name: ")
    outfile.write(name + "\n")
outfile.close()

infile = open("neighbors.txt", "r")
names_in_file = infile.read()
infile.close()
print(names_in_file)

infile = open("neighbors.txt", "r")
line = infile.readline()
print(line)
line = infile.readline()
print(line)
line = infile.readline()
print(line)
line = infile.readline()
print(line)
line = infile.readline()
print(line)
line = infile.readline()
print(line)
infile.close()

infile = open("neighbors.txt", "r")
line = infile.readline()
line = line.rstrip("\n")
print(line)
line = infile.readline()
line = line.rstrip("\n")
print(line)
line = infile.readline()
infile.close()

infile = open("neighbors.txt", "r")
line = infile.readline()
while line != "":
    line = line.rstrip("\n")
    print(line)
    line = infile.readline()
infile.close()
