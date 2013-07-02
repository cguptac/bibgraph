import errors
import operator

class base_graph:
    def __init__(self):
        self.graph = {}

    def addtonode(self, nodeId, data):
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
        if self.graph.has_key(nodeId)==False:
            self.graph.update({nodeId:set([])})
        else:
            print """
                  Useage: newnode(self, nodeId)
                  self.graph already has a node called %s
                  """ %nodeId
            raise errors.NodeError("nodeId %s already exists" %nodeId)



    def removefromnode(self, nodeId, data):
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
        return self.graph.pop(nodeId, 'node not found')

    def __getitem__(self, key):
        return self.graph[key]

    def counts(self, keylist, filter=False, sort=True):
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

            if filter==True:
                for x in keylist:
                    try:
                        tmp.pop(x)
                    except KeyError:
                        pass

            if sort==True:
                sorted_tmp = sorted(tmp.iteritems(), key=operator.itemgetter(1), reverse=True)
                tmp = sorted_tmp

            return tmp
        else:
            raise errors.ListOrSet('keylist needs to be either a list or a set')
