# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
total = 0
# global variable for count

def solution(A, B, T):
    dfs(A,B,T)
    global total
    return total

def dfs(A,B,T):
    
    # A < x < B

    if( A < T.x and T.x < B ):
    # Check first if root value is between A and B

        if (T.l is None):
            l_truth = True
        else: 
            l_truth = dfs(A,B,T.l)
        # Check left tree, if tree dne, tree counts as true

        if (T.r is None):
            r_truth = True
        else:
            r_truth = dfs(A,B,T.r)
        # Check right tree, if tree dne, tree counts as true

        t_truth = l_truth and r_truth
        # Only if both subtrees are true, will the current tree be true

        if t_truth:
            global total
            total += 1
            return True

        else:
            return False

    else:
        return False