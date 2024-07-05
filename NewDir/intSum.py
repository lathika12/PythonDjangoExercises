def fix_teen(n):
    val = 0 if (n>= 13 and n<15) or ( n > 16 and  n <=19) else n
    return val

def no_teen_sum(*args):
    l = list(args)
    sum=0
    for i in l:
        sum = sum + fix_teen(i)
    print(sum)

def __main__(*args):
    print("Main method")
    no_teen_sum(2, 16, 14)

__main__()