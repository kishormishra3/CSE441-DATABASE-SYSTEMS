import sys
disk_variable={}
inst=[]
file=open(sys.argv[1])
s=file.readline()
i=0
start=None
end=None
comm=[]
while(s):
    if i==0:
        s=s.split()
        for j in range(len(s)):
            if j%2==0:
                disk_variable[s[j]]=int(s[j+1])
    elif s.strip():
        s=s[1:-2]
        inst.append(s)
        if 'START CKPT' in s:
            start=i-2
        if 'END CKPT' in s:
            end=i-2
    i+=1
    s=file.readline()
if start==None and end != None:
    sys.exit()
elif start!=None and end == None:
    temp=inst[start]
    inst.reverse()
    temp=temp[temp.find('(')+1:temp.find(')')]
    temp=temp.replace(',',"")
    ckpt=temp.split()
    for i in inst:
        if 'COMMIT' in i:
            comm.append(i.split()[1])
        elif i[0]=='T':
            i=i.replace(' ','')
            i=i.split(",")
            if i[0] not in comm:
                disk_variable[i[1]]=int(i[2])
        elif 'START' in i and 'CKPT' not in i:
            i=i.split()
            if i[1] in ckpt:
                ckpt.remove(i[1])
        if len(ckpt)==0:
            break
elif start ==None and end ==None:
    inst.reverse()
    for i in inst:
        if 'COMMIT' in i:
            comm.append(i.split()[1])
        elif i[0]=='T':
            i=i.replace(' ','')
            i=i.split(",")
            if i[0] not in comm:
                disk_variable[i[1]]=int(i[2])
elif start !=None and end !=None:
    inst=inst[start:]
    inst=inst[1:-1]
    for i in inst:
        if 'COMMIT' in i:
            comm.append(i.split()[1])
        elif i[0]=='T':
            i=i.replace(' ','')
            i=i.split(",")
            if i[0] not in comm:
                disk_variable[i[1]]=int(i[2])
output_file=open("2019201038_2.txt","w")
temp=""
for i in sorted(disk_variable):
    temp=temp+i+" "+str(disk_variable[i])+" "
temp=temp[:-1]
temp+="\n"
output_file.write(temp)
            
