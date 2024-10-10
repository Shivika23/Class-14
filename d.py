f1 = input("Enter the name of the first file: ")
f2 = input("Enter the name of the second file: ")

file1 = open(f1, 'r')
file2 = open(f2, 'r')

print("Content of the first file before appending: \n", file1.read())
print("Content of the second file before appending: \n", file2.read())

file1.close()
file2.close()

file1 = open(f1, 'a+')
file2 = open(f2, 'r')

file1.write(file2.read())
file1.seek(0)
file2.seek(0)

print("Content of the first file before appending: \n", file1.read())
print("Content of the second file before appending: \n", file2.read())

file1.close()
file2.close()