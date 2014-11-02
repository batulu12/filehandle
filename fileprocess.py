f = open('C:\useful\ljscrapy\ljscrapy\lj\download_middleware\gent56.txt')
list = f.readlines()
fw = file('C:\useful\ljscrapy\ljscrapy\lj\download_middleware\chu4.txt','w')
for l in list:
   t = l.split(' ')
   fw.write(t[1]+' '+t[2]+'\r\n')
fw.close()
f.close()