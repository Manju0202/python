#Break

for i in range(11):
   
    if i==7:
        break
    print(i)
    
#while break
i=0
while(i<=11):
    i+=1
    if i==7:
        break
    print(i)
#continue

for i in range(11):
    if i==7:
        continue
    print(i)
# while continue
i=0
while(i<=11):
    i+=1
    if i==7:
        continue
    print(i)
#pass

for i in range(11):
    if 1==7:
        pass
    print(i)
    
# print 1st 4 letters of ur name(for loop):
x='manju'
for i in x:
        if i=='u':
            break
        print(i)
        
# skip 5th character from ur name(for loop):
x='manjujayaram'
for i in x:
    if i=='u':
        continue
    print(i)

x='jubliee'
for i in x:
   
