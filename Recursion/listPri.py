def lis(li,a):
    # a = len(li)

    if a == 0:
        print(li[a])
        # return
    else:
        lis(li,a-1)
        print(li[a])

t = [12,23,34,45]
lis(t,len(t)-1) 