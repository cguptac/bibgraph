import errors
import operator

class base_graph:
    def __init__(self):
        self.graph = {}

    def addtonode(self, nodeId, data):
        """
useage: obj.addtonode(nodeId, data)
nodeId has to be an existing node on the graph
data has to be a list or set of the same type of elements as nodeId

If nodeId is not found, a KeyError is raised.
If data does not have type 'list' or 'set, an errors.ListOrSet
error is raised.
        """
        if (type(data)==set) | (type(data)==list):
            try:
                self.graph[nodeId].update(set(data))
            except KeyError:
                print "Node %s does not exist" %(nodeId)
                raise 
        else:
            print """
                  Useage: addtonode(self, nodeId, data)
                  Input data type is %s, should be one of <type 'list'> or <type 'set'>
                  """ %(type(data))
            raise errors.ListOrSet("must provide type 'list' or type 'set'")
            

    def newnode(self, nodeId):
        """
    useage: obj.newnode(nodeId)
    creates a new node on the graph with id nodeId
    the edges corresponding to this node are initialized as empty.

    If the graph already has a node with id nodeId, an
    errors.NodeError is raised.
        """
        if self.graph.has_key(nodeId)==False:
            self.graph.update({nodeId:set([])})
        else:
            print """
                  Useage: newnode(self, nodeId)
                  self.graph already has a node called %s
                  """ %nodeId
            raise errors.NodeError("nodeId %s already exists" %nodeId)



    def removefromnode(self, nodeId, data):
        """
    useage: obj.removefromnode(nodeId, data)

    nodeId is the id of the node on the graph.
    data is the set of edges to be removed from the node.

    If the type of data is not list or set, an errors.ListOrSet
    error is raised.

    If nodeId does not exist, a KeyError is raised.
        """
        if (type(data)==list) | (type(data)==set):
            try:
                self.graph[nodeId] = self.graph[nodeId] - set(data)
            except KeyError:
                print "Node %s does not exist" %(nodeId)
                raise 
        else:
            print """
                  useage: removefromnode(self, nodeId, data)
                  data must be <type 'list'> or <type 'set'>
                  """
            raise errors.ListOrSet('input should be either a list or a set')

    def delnode(self, nodeId):
        """
    useage: obj.delnode(nodeId)

    nodeId is the ID of the node on the graph to be deleted.
        """
        return self.graph.pop(nodeId, 'node not found')

    def __getitem__(self, key):
        """
    useage: obj[key]

    returns the data stored at the key. If the key is not present, a KeyError
    is raised.
        """
        return self.graph[key]

    def counts(self, keylist, filterQ=False, sortQ=True):
        """
    useage: histogram = obj.counts(keylist, filterQ=False, sortQ=True)

    keylist is the list of keys for which the data is used to compute the
    counts for the edge histogram. The returned histogram is a dictionary
    with keys the data entries corresponding to entries in keylist
    and the counts corresponding to these keys are the values.

    filterQ, if True, removes the entries of keylist from the keys for
    the histogram.

    sortQ, if False, returns the dictionary. If sortQ=True, then a list
    or tuples is returned, with the tuples arranged by descending
    values of the counts in the histogram.

    If type(keylist) is different from 'list' or 'set', an errors.ListOrSet
    error is raised.
        """
        tmp = {}
        if (type(keylist)==list) | (type(keylist)==set):
            for x in keylist:
                if self.graph.has_key(x):
                    for y in self.graph[x]:
                        try:
                            tmp[y] = tmp[y]+1
                        except KeyError:
                            tmp.update({y:int(1)})
                else:
                    pass

            if filterQ==True:
                for x in keylist:
                    try:
                        tmp.pop(x)
                    except KeyError:
                        pass

            if sortQ==True:
                sorted_tmp = sorted(tmp.iteritems(), key=operator.itemgetter(1), reverse=True)
                tmp = sorted_tmp

            return tmp
        else:
            raise errors.ListOrSet('keylist needs to be either a list or a set')
