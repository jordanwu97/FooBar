
from __future__ import generators
from fractions import Fraction as fr
#PART 1
#I FIRST CREATED A ITERATIVE FUNCTION TEST1 FOR FINDING TERMINATING PAIRS. IT WAS EXTREMELY INEFFICENT.
#BY GENERATING A SMALL SEQEUENCE, I CREATED TEST2 WHICH ACHIEVES O(1)


def createGraph(bananalist):

    s = set() #Generate a set of 2^k's
    y=1

    for x in xrange(33):
        y = y * 2
        s.add(y)
    
    def test1(num):
        #Original iterative algorithm. Does not actually achieve O(n). 
        #High memory usage and time complexity when given pairs with long loops
        a = num[0]
        b = num[1]
        l = set()
        count = 0

        while True:

            count += 1

            if a in l or b in l:
                return False

            if a == b:

                return True

            if a > b:
                l.add(a)
                a -= b
                b += b
            elif b > a:
                l.add(a)
                b -= a
                a += a

    def generateList():
    #Generates a list from test1 algorithm for finding patterns
        t = open('trues', 'w')

        for i in range(1,20):
            for j in range(1,4000):
                a = test1((i,j))

                if a[0] == True :
                    # print a
                    t.write(str(a[1])+"\n")

        t.close()

    def test2(num):
    #O(1) algorithm. Created by plugging generated list into OEIS
        c = min(num[0],num[1])
        t = num[0]+num[1]
    
        frac_t = fr(t,c).numerator
    
        if t in s or frac_t in s: #SOMEHOW, TERMINATING PAIR'S SUM OR THEIR REDUCED FRACTION FALLS INTO THE SET OF 2^k
            return True
        else:
            return False

    def verification():
    #Verification loop over x amount of random points
        a = True
        b = True
        count = 0
        false_pos = []
        for i in xrange(1,20):
            for j in xrange(1,2000):
                r = (i,j)
                a = test1(r)[0]
                b = test2(r)
                if not a == b:
                    print(a,b)

        print false_pos
            
    def createEdges(l):
    #Creates graph G such that iter(G) contains vertices, G[v] contains vertices adjacent to v
        graph = {} #empty graph

        for x in xrange(len(l)):
            adjacent_vertices = set() #empty set
            for y in xrange(0,len(l)):
                if not test2((l[x] , l[y])):
                    adjacent_vertices.add(y) #add neighbor to set if fails test
    
            graph[x] = adjacent_vertices #set of neighbors as dict[v]
    
        return graph

    Graph = createEdges(bananalist)
    
    return Graph

#PART 2
#FOR MAXIMUM MATCHING OF GRAPH GENERATED IN PART 1, I USED DR. DAVID EPPSTEIN'S IMPLEMENTATION OF EDMOND'S BLOSSOM ALGORITHM

# Find maximum cardinality matching in general undirected graph
# D. Eppstein, UC Irvine, 6 Sep 2003

if 'True' not in globals():
    globals()['True'] = not None
    globals()['False'] = not True

class unionFind:
    '''Union Find data structure. Modified from Josiah Carlson's code,
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
to allow arbitrarily many arguments in unions, use [] syntax for finds,
and eliminate unnecessary code.'''

    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        '''Find the root of the set that an object is in.
Object must be hashable; previously unknown objects become new singleton sets.'''

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object
        
        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
        
        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, *objects):
        '''Find the sets containing the given objects and merge them all.'''
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

def matching(G, initialMatching = {}):
    '''Find a maximum cardinality matching in a graph G.
G is represented in modified GvR form: iter(G) lists its vertices;
iter(G[v]) lists the neighbors of v; w in G[v] tests adjacency.
The output is a dictionary mapping vertices to their matches;
unmatched vertices are omitted from the dictionary.

We use Edmonds' blossom-contraction algorithm, as described e.g.
in Galil's 1986 Computing Surveys paper.'''

    # Copy initial matching so we can use it nondestructively
    matching = {}
    for x in initialMatching:
        matching[x] = initialMatching[x]


    # Form greedy matching to avoid some iterations of augmentation
    for v in G:
        if v not in matching:
            for w in G[v]:
                if w not in matching:
                    matching[v] = w
                    matching[w] = v
                    break

    def augment():
        '''Search for a single augmenting path.
Return value is true if the matching size was increased, false otherwise.'''
    
        # Data structures for augmenting path search:
        #
        # leader: union-find structure; the leader of a blossom is one
        # of its vertices (not necessarily topmost), and leader[v] always
        # points to the leader of the largest blossom containing v
        #
        # S: dictionary of leader at even levels of the structure tree.
        # Dictionary keys are names of leader (as returned by the union-find
        # data structure) and values are the structure tree parent of the blossom
        # (a T-node, or the top vertex if the blossom is a root of a structure tree).
        #
        # T: dictionary of vertices at odd levels of the structure tree.
        # Dictionary keys are the vertices; T[x] is a vertex with an unmatched
        # edge to x.  To find the parent in the structure tree, use leader[T[x]].
        #
        # unexplored: collection of unexplored vertices within leader of S
        #
        # base: if x was originally a T-vertex, but becomes part of a blossom,
        # base[t] will be the pair (v,w) at the base of the blossom, where v and t
        # are on the same side of the blossom and w is on the other side.

        leader = unionFind()
        S = {}
        T = {}
        unexplored = []
        base = {}
        
        # Subroutines for augmenting path search.
        # Many of these are called only from one place, but are split out
        # as subroutines to improve modularization and readability.
        
        def blossom(v,w,a):
            '''Create a new blossom from edge v-w with common ancestor a.'''
            
            def findSide(v,w):
                path = [leader[v]]
                b = (v,w)   # new base for all T nodes found on the path
                while path[-1] != a:
                    tnode = S[path[-1]]
                    path.append(tnode)
                    base[tnode] = b
                    unexplored.append(tnode)
                    path.append(leader[T[tnode]])
                return path
            
            a = leader[a]   # sanity check
            path1,path2 = findSide(v,w), findSide(w,v)
            leader.union(*path1)
            leader.union(*path2)
            S[leader[a]] = S[a] # update structure tree

        topless = object()  # should be unequal to any graph vertex
        def alternatingPath(start, goal = topless):
            '''Return sequence of vertices on alternating path from start to goal.
Goal must be a T node along the path from the start to the root of the structure tree.
If goal is omitted, we find an alternating path to the structure tree root.'''
            path = []
            while 1:
                while start in T:
                    v, w = base[start]
                    vs = alternatingPath(v, start)
                    vs.reverse()
                    path += vs
                    start = w
                path.append(start)
                if start not in matching:
                    return path     # reached top of structure tree, done!
                tnode = matching[start]
                path.append(tnode)
                if tnode == goal:
                    return path     # finished recursive subpath
                start = T[tnode]
                
        def pairs(L):
            '''Utility to partition list into pairs of items.
If list has odd length, the final pair is omitted silently.'''
            i = 0
            while i < len(L) - 1:
                yield L[i],L[i+1]
                i += 2
            
        def alternate(v):
            '''Make v unmatched by alternating the path to the root of its structure tree.'''
            path = alternatingPath(v)
            path.reverse()
            for x,y in pairs(path):
                matching[x] = y
                matching[y] = x

        def addMatch(v, w):
            '''Here with an S-S edge vw connecting vertices in different structure trees.
Find the corresponding augmenting path and use it to augment the matching.'''
            alternate(v)
            alternate(w)
            matching[v] = w
            matching[w] = v
            
        def ss(v,w):
            '''Handle detection of an S-S edge in augmenting path search.
Like augment(), returns true iff the matching size was increased.'''
    
            if leader[v] == leader[w]:
                return False        # self-loop within blossom, ignore
    
            # parallel search up two branches of structure tree
            # until we find a common ancestor of v and w
            path1, head1 = {}, v
            path2, head2 = {}, w
    
            def step(path, head):
                head = leader[head]
                parent = leader[S[head]]
                if parent == head:
                    return head     # found root of structure tree
                path[head] = parent
                path[parent] = leader[T[parent]]
                return path[parent]
                
            while 1:
                head1 = step(path1, head1)
                head2 = step(path2, head2)
                
                if head1 == head2:
                    blossom(v, w, head1)
                    return False
                
                if leader[S[head1]] == head1 and leader[S[head2]] == head2:
                    addMatch(v, w)
                    return True
                
                if head1 in path2:
                    blossom(v, w, head1)
                    return False
                
                if head2 in path1:
                    blossom(v, w, head2)
                    return False    

        # Start of main augmenting path search code.

        for v in G:
            if v not in matching:
                S[v] = v
                unexplored.append(v)

        current = 0     # index into unexplored, in FIFO order so we get short paths
        while current < len(unexplored):
            v = unexplored[current]
            current += 1

            for w in G[v]:
                if leader[w] in S:  # S-S edge: blossom or augmenting path
                    if ss(v,w):
                        return True

                elif w not in T:    # previously unexplored node, add as T-node
                    T[w] = v
                    u = matching[w]
                    if leader[u] not in S:
                        S[u] = w    # and add its match as an S-node
                        unexplored.append(u)
                        
        return False    # ran out of graph without finding an augmenting path
                        
    # augment the matching until it is maximum
    while augment():
        pass

    return matching


#END OF MAXIMUM MATCHING ALGORITHM


def answer(bananalist): 
    Graph = createGraph(bananalist)
    m = matching(Graph)

    return len(bananalist) - (len(m))
    
print(answer([1,1]))
print(answer(range(1, 100000000)))