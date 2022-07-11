
while True:
    a=input("转化信息？\n")
    a.upper()
    b=list(a)
    c=[]
    st = 0
    rd = 0
    d="|"
    s=0 
    for x in b:
        s=(ord(x))-96
        st=s//5
        if s%5!=0:
            st+=1
        rd=s%5
        if rd==0:
            rd=5
        st=str(st)
        rd=str(rd)
        d=d+st+rd+"|" 
    print(d)
#b=input("")
