import random
fd = open('C:\useful\ljscrapy\ljscrapy\lj\download_middleware\chu2.txt','r')
li2 = fd.readlines()
li = li2[0].split('\r')
for l in li:
    print l
length = len(li)
index = random.randint(0, length -1)
item = li[index]
t  = item.split(' ')
request = 'http://%s:%s' % (t[0],t[1])
fd.close()