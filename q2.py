for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sum(a)
    c=n
    for t in a:
        if not t:
            c+=-1
    if k<100:
        print('NO')
    elif k == 100:
        print('YES')
    else:
        if k >= 100+c:
            print('NO')
        else:
            print('YES')