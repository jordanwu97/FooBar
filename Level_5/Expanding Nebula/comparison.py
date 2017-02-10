from version1 import answer as v1answer
from version2 import answer as v2answer
from random import randint
from time import time

def createRandomGrid():
    h = randint(9,10)
    w = randint(40, 50)

    g = []
    for y in xrange(h):
        row = []
        for x in xrange(w):
            row.append(randint(0,1))
        g.append(row)
    
    return g,w,h

x = []
y = []
for n in xrange(10):
    g,w,h = createRandomGrid()
    t1 = time()

    n = v2answer(g)

    print time() - t1

