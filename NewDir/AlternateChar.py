str = "Hw"
ls = list(str)
print("".join(ls[::2]))


# End Other
s1 = "Hiabs"
s2 = "ABS"
len = len(s2)
print(len)
if s1[len-1:].lower() == s2.lower():
    print(True)
else:
    print(False)


#Double Char
dblc = "The"
ls = [x*2 for x in dblc]
print("ls: " , ls)
ls3 = ["".join(x) for x in ls]
print("".join(ls3))

# #No. of even integers
# l = [1,2,3,4,5,6,7,8,9]
#
# even = [ i for i in l if i%2 ==0 ]
# print(len(even))

