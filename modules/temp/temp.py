import time
import graph
import qa
from numpy import random


t1 = time.time()
s = qa.random_graph.make_graph(10000, 50, 100000)
print time.time() - t1, "seconds"
t1 = time.time()
cup = s.upstr.counts([int(random.random() * 100000) for x in range(50)])
print time.time() - t1, " seconds"
t1 = time.time()
cdn = s.upstr.counts([int(random.random()*100000) for x in range(50)])
print time.time() - t1, "seconds"
