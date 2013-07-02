import base_graph as bg
import inspect
import errors

class graph:
    def __init__(self):
        self.upstr = bg.base_graph()
        self.dnstr = bg.base_graph()
        print """
    This is a temporary message that will be displayed till it is disabled.
    The place to disable this message is in module %s.

    The following convention is used: If A cites B, then A is DOWNSTREAM
    of B. B is UPSTREAM of A.

    Similarly, if A is cited by B, A is UPSTREAM of B, while B is
    DOWNSTREAM of A.
              """ %(str(inspect.stack()[0][1]))

    
    def add_upstr(self, nodeId, data):
        # error checking
        if (type(data)==list) | (type(data)==set):
            try:
                self.upstr.addtonode(nodeId, data)
            except KeyError:
                self.upstr.newnode(nodeId)
                self.upstr.addtonode(nodeId, data)
            for x in data:
                try:
                    self.dnstr.addtonode(x, [nodeId])
                except KeyError:
                    self.dnstr.newnode(x)
                    self.dnstr.addtonode(x, [nodeId])
        else:
            raise errors.ListOrSet("type provided is %s, but required type is 'list' or 'set'" % type(data))

    
    def add_dnstr(self, nodeId, data):
        # error checking
        if (type(data)==list) | (type(data)==set):
            try:
                self.dnstr.addtonode(nodeId, data)
            except KeyError:
                self.dnstr.newnode(nodeId)
                self.dnstr.addtonode(nodeId, data)
            for x in data:
                try:
                    self.upstr.addtonode(x, [nodeId])
                except KeyError:
                    self.upstr.newnode(x)
                    self.upstr.addtonode(x, [nodeId])
        else:
            raise errors.ListOrSet("type provided is %s, but required type is 'list' or 'set'" % type(data))
