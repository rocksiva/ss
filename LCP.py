b=input(input())
m=[]
i=[]
m1=[]
for i in range (b):
    i.append( len(m[i]))
s=min(i)
if(s!=1):
     i=0
     for j in range(0,s):
          if((m[i][j]==m[i+1][j])):
             m1.append(m[i][j])
print(*m1,sep=' ')
