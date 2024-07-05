ls = [1,4,3,4,5,6,1,2,1,8,9,10]
chk = [1,2,3]
chklen = len(chk)
b = False

for i in range(0,len(ls)):
    print("i: " , i)
    tmp = ls[i:i+chklen]
    if chk == tmp:
        print("chk : " , chk , "tmp: " , tmp)
        b = True
        break

print(b)