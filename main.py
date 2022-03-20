n=int(input())
num=[1,2,3,4,5,6,7,8,9]
temp=[]
for val in num:
    new_n=str(n)
    #new_n = new_n[:1] + str(val) + new_n[1:]
    inc=1
    for c in range(0,len(str(new_n))+1,1):
        #new_n = (new_n[:len(str(n))+c]+str(val)+new_n[len(str(n))+c+1:])
        new_n = str(val)+new_n[:(inc)]+new_n[(inc+1):]
        print(new_n)
        if int(new_n) % 9 == 0:
            temp.append(int(new_n))
        inc=inc+1
        new_n=str(n)
    new_b = new_n[:1] + new_n[1:] + str(val) 
    new_e = str(val) + new_n[:1] + new_n[1:]
    new_n, new_b, new_e =int(new_n), int(new_b), int(new_e)
    if new_b % 9 == 0:
        temp.append(new_b)
    if new_e % 9 == 0:
        temp.append(new_e)
least=temp[0]
print(temp)
print(temp)
for tem in temp:
    if int(tem)<int(least):
        least=tem
print(least)
