def einstein():
    print("This is a puzzle favored by Einstein.You will be asked to enter\n a three digit number,where the hundred's digit differs from the\n one's digit by at least two.The procedure will always yield 1089")
    num=int(input("Give me a number:"))
    rev_num=str(num)[::-1]
    print(f"For the number:{num} the reverse number is: {rev_num}")
    x=max(num,int(rev_num))
    n=min(num,int(rev_num))
    differ=x-n
    print(f"The difference between {x} and {n} is {differ} ")
    rev2_num=str(differ)[::-1]
    print(f"The reverse difference is:{rev2_num}")
    sum=int(rev2_num)+differ
    print(f"The sum of:{differ} and revDiff is:{sum}")
einstein()