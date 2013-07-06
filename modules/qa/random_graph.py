import numpy
import sys
import string
import random

rnd = numpy.random
sys.path.append('./../')
import graph


def make_graph(m,n, l):
    s = graph.graph()
    keys = random_string(l, m)
    keys = set(keys)

    for key in keys:
        tmp = random_string(l,n)
        tmp = set(tmp)
        r = rnd.random()
        if r>0.5:
            s.add_upstr(key, tmp)
        else:
            s.add_dnstr(key, tmp)
    return s


def random_string(l, m):
    return [''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(l)) for x in range(m)]
    

    
