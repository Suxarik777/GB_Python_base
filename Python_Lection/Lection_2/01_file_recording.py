with open('file3.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')


colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()

colors = ['red', 'green', 'blue']
data = open('file2.txt', 'w')
data.write('line 1\n')
data.write('line 2\n')
# data.writelines(colors) # разделителей не будет
data.close()
