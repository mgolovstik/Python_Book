test = open('/home/mgolovstik/Python_Book/mytest.txt','w')
test.write('jsdfhksdhbxdchfsj\n')                             
test.close()


test = open('/home/mgolovstik/Python_Book/mytest.txt')
print(test.read())
