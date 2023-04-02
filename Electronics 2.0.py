def b2d(list1):
    num=list1[::-1]
    
    d=[int(num[i])*(2**i) for i in range(len(num))]
    return sum(d)


def o2d(list1):
    num=list1[::-1]
    
    d=[int(num[i])*(8**i) for i in range(len(num))]
    return sum(d)


def h2d(list1):
    num=list1[::-1]
    hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    d=[hexa.index(num[i])*(16**i) for i in range(len(num))]
    return sum(d)


def d2h(num):
    num=int(num)
    hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    rem=[]
    while(num!=0):
        rem.append(num%16)
        num//=16
    rem=rem[::-1]
    return ''.join([str(hexa[rem[i]]) for i in range(len(rem))])


def d2b(num):
    num=int(num)

    rem=[]
    while(num>0):
        rem.append(num%2)
        num//=2
    rem=rem[::-1]
    return int(''.join([str(rem[i]) for i in range(len(rem))]))


def d2o(num):
    num=int(num)
    rem=[]
    while(num!=0):
        rem.append(num%8)
        num//=8
    rem=rem[::-1]
    return int(''.join([str(rem[i]) for i in range(len(rem))]))

    
print("\n")
while True:
    print("Enter 0b, 0x, 0o at beginning to differentiate binary, hexadecimal and octal")
    x=input("Enter your input:")

    list1=[x.upper() for x in str(x)]
    t=''.join(str(i) for i in list1[:2])
    print(t)
    list1=list1[2:]
    type=sorted(set(list1))

    result=[0,0,0]
    try:
        if(all(int(i) <2 for i in type) and t=="0B"):
            result[0]=1
            choice=0

    except:
        result[0]=0
    try:
        #if((isinstance(i, int) for i in type) or any(i.isalpha() for i in type)):
        if(all(i in '0123456789abcdefABCDEF' for i in type) and t=="0X"):
            result[1]=1
            choice=1

    except:
        result[1]=0
    try:
        if(all(int(i) <8 for i in type) and t=="0O"):
            result[2]=1
            choice=2
    except:
        result[2]=0

    if(all(int(i)==0 for i in result)):
        print("Wrong Input")
        continue
    break

        


if(choice==0):
    h=d2h(b2d(list1))
    o=d2o(b2d(list1))
elif(choice==1):
    b=d2b(h2d(list1))
    o=d2o(h2d(list1))
elif(choice==2):
    b=d2b(o2d(list1))
    h=d2h(o2d(list1))
    
i=0
print("For the given input and choice of number sytem")
if(choice!=0):
    print("\t{}. Binary number     : {}".format(i,b))
    i+=1

if(choice!=1):
    print("\t{}. Hexadecimal number: {}".format(i,h))
    i+=1

if(choice!=2):
    print("\t{}. Octal number      : {}".format(i,o))
    i+=1   

