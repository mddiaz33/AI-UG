from bs4 import BeautifulSoup, SoupStrainer
from bs4.dammit import EncodingDetector
import httplib2
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

from bs4 import BeautifulSoup
import urllib.request


class Tree(object):
    "Generic tree node."
    def __init__(self, state='root', children=None, parent=None):
        self.state = state
        self.children = []
        self.parent = parent
        if children is not None:
            for child in children:
                print("adding kid"+ child)
                self.add_child(child)


    def __repr__(self):
        return self.state

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


class Problem(object):
    frontier = []
    explored = []
    solution = []

    def __init__(self, initial = "", goal = "" ):
        self.initial = initial
        self.goal = goal

    def __repr__(self):
        return self.initial

    def goalTest(self, node):
        print("running goal test")
        if node == self.goalTest:
            return True
        return False

    def getKids(self,url):
        list = []
        print("Getting kids")
        http = httplib2.Http()
        status, response = http.request(url)

        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                list.append(link['href'])

        return list

    #get path
    def getSolution(self,node):
        print("Getting solution")
        if node.parent is not None:
            self.solution.append(node)
            return self.getSolution(node.parent)
        return self.solution


    def inExplored(self, node) :
        print("checking explored")
        for x in self.explored:
            if node == x:
                return True
        return False

    def inFrontier(self, node) :
        print("checking frontier")
        for f in self.frontier:
            if node == f:
                return True
        return False

#runs breadth first search
    def bfs(self):
        node = Tree(self.initial)
        print("1")
        if self.goalTest(node):

            return self.getSolution(node)


        frontier = self.getKids(node.state)
        print(frontier)
        for  x in frontier:
            node.children.append(x)

        while frontier is not None:
            if frontier is None:
                return []
            self.explored.append(node)

            for child in node.children:
               if not self.inExplored(child) and not self.inFrontier(child):
                    if self.goalTest(child):
                        return self.getSolution(child)
                    print("adding child to frontier")
                    self.frontier.append(child)



test1 = Problem("https://www.onlinegdb.com/online_python_compiler","https://slack.com/lp/three?&utm_medium=display&utm_source=carbon&utm_campaign=d_display_carbon_row_en_design_ob-p_cr-plain_ym-201807&dclid=CPTNnbfVteMCFVA7TwodAgMBuw" )
solution1 = test1.getKids(test1.initial)
print(solution1)
print(solution1)
print(test1.bfs())
