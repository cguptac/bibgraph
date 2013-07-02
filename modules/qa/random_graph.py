import numpy
import sys

rnd = numpy.random
sys.path.append('./../')
import graph


def make_graph(m,n, N):
    s = graph.graph()
    keys = rnd.lognormal(1, 1, m)
    keys = set([int(key * N) for key in keys])

    for key in keys:
        tmp = rnd.lognormal(1, 1, n)
        tmp = [int(t * N) for t in tmp]
        r = rnd.random()
        if r>0.5:
            s.add_upstr(key, tmp)
        else:
            s.add_dnstr(key, tmp)
    return s


    
