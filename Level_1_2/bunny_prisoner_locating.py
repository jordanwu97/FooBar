def answers(x,y):
    m = 1
    for j in range(1, y):
        m = m + j
    print m
    num = y - 1
    n = 0
    for i in range(y+1,y+x):
        n = n + i
    print n + m

    # for i in range(1,x+1):
    #     n = n + i
    # print n
# answers(input(),input())
