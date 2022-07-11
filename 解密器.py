while True:
    shuru = input("解密信息：\n")
#asd qwer
    jieguolist = []
    jieguo = ''
    zuizhongjieguo = ''
    shurulist = list(shuru)
    for x in shurulist:
        if x == "|":
            shurulist.remove(x)
# 删除“|”
# ---------------------------------------------------------#
    a = shurulist[::2]
    b = shurulist[1::2]
    shuchu = ''
    for x in range(len(a)):
        aa = int(a[x])
        bb = int(b[x])

#    if bb == 5:
#        bb = 0
        if aa == 1:
            aa = 0
        if aa != 0:
            aa = aa - 1
            aa = aa * 5
        shuchu = aa + bb
        shuchu1 = chr(shuchu + 96)
        jieguolist.append(shuchu1)
    #print(shuchu1)
    for x in jieguolist:
        jieguo = jieguo + x
    print(jieguo)

