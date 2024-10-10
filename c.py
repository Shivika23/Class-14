file = open('sample_doc.txt', 'r')
a = 0
b = file.read()
c = b.split('\n')

for i in c:
    if i:
        a+=1

print(a)
