# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    S = S.upper() 
    S = S.replace("-","")
    # make all upper case and wipe "-"

    l = len(S)
    remainder = l % K
    q = l / K
    additional = 0
    # remainder = offset for the first group.
    # q = how many times "-" will be added
    # additional will be incremented whenever "-" is added,
    # as adding "-" will bump the alpha-num character to the next index

    stlist = list(S)
    # change to list to use insert function

    if not remainder == 0:
    	stlist.insert(remainder,'-')
    	additional += 1

    #first set of remainder an-chars

    for n in xrange(1,q):
    	stlist.insert((K*n)+remainder+additional,'-')
    	additional += 1

    #loop thru, inserting "-" at each (K*n) spot while accounting for offsets caused by remainder and additional

    S = ''.join(stlist)
    return S

print solution('2-4A0r7-4k',5)