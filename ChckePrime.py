def prime(n):
    f = False
    if n ==1:
        print('Not prime')
    elif n>1:
        for i in range(2,n):
            if n%i == 0:
                f = True
                break
        if f == True:
            print('Not prime as flage false')
        else: print('Prime  as flage True')


prime(6)

