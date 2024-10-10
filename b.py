file = open('Codingal.txt', 'r')
print("File in read mode...")
print(file.read())
file.close()

file_2 = open('Codingal.txt', 'w')
print("File is in the write mode...")
file_2.write('Hi i am shivika')
file_2.close()

file_3 = open('Codingal.txt', 'a')
print("File is in the append mode...")
file_3.write(' and i am shivika 2.0')
file_3.close()