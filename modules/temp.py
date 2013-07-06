import time
import graph
import qa
from numpy import random


t1 = time.time()
s = qa.random_graph.make_graph(10000, 50, 100000)
print time.time() - t1, "seconds"
t1 = time.time()
N=1000000
cup = s.upstr.counts(set(int(random.random() * 100000) for x in xrange(N)))
print time.time() - t1, " seconds"
t1 = time.time()
cdn = s.upstr.counts(set(int(random.random()*100000) for x in xrange(N)))
print time.time() - t1, "seconds"


