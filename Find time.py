
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst=list()
dic=dict()
tmp=list()
tmp2=list()
for line in handle:
    if line.startswith('From'):
        line=line.rstrip()
        line=line.split()
        try:
            x=line[3]
        except:
            continue
        a,b,c,d,e,f,g=line
        lst.append((a,b,c,d,e,f,g))
for (a,b,c,d,e,f,g) in lst:
    time=f
    time= time.split(':')
    hr=time[0]
    dic[hr] = dic.get(hr, 0) +1
tmp2=sorted(dic.items(), reverse=False)
for a,b in tmp2:
    print(a,b)
