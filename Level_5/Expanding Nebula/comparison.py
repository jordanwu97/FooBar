from version1 import answer as v1answer
from version2 import answer as v2answer
from random import randint
from time import time

def createRandomGrid():
    h = randint(6, 9)
    w = randint(45, 50)
    g = []
    for y in xrange(h):
        row = []
        for x in xrange(w):
            row.append(randint(0,1))
        g.append(row)
    
    return g

for n in xrange(10):
    g = createRandomGrid()
    t1 = time()
    n = v2answer(g)
    print time() - t1
