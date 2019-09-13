
class Node:
    def __init__(self, state, parent=None, pathCost=None, children=None):
        self.state = state
        self.children  = children
        self.parent = parent
        self.pathCost = pathCost


    def __str__(self):
        return str(self.state)
class problem:
    def __init__(self):
        self.actions = [[0,2,1],[2,0,1],[1,1,1],[1,0,1],[0,1,1]],[0,2,0],[2,0,0],[1,1,0],[1,0,0],[0,1,0]]
        self.initialState = [3,3,1]


    def goalTest(state):
     return state == [0,0,0]

    def canMove(self, action):
        state = self.state
        if action[2] == state.pop(2):
            return [-1,-1,-1]

        elif action[2] == 0:
                 return [state.pop - action.pop, state.pop - action.pop , 0]


        elif action[2] == 1:
                 return [state.pop + action.pop, state.pop + action.pop, 1]
    def isDead(nState):
        dead = [[2,3,0][1,3,0][1,3,0],[2,0,1],[2,1,1][1,0,1]]
        for x in dead:
            if nState ==  dead[x]:
                return True

        return False

    def isValid(nState):
       for x in nState:
           if x <= 0 or x >= 4:
               return False



        return True


def getSolution(currNode):
    #return shortest path
    path=[]

    while currNode.parent != None:
    path.append(currNode.parent)
    _currNode = currNode.parent

    return path


def breadthFirstSearch(start):

    nNode = Node(Node)

    if nNode.goalTest(nNode.state):
        return nNode.getSolution


    explored = []

    frontier = Node(problem.initialState) # a FIFO QUE WITH ONLY ONE NODE


    while True:
        if frontier.isEmpty:
            return False

         curr: Node = frontier.pop
        explored.append(curr)
         _currstate = curr.state

            for x in problem.actions:
                currchild =  Node(problem.canMove(Node,problem.actions[x]))

                if problem.isValid(currchild.state) and not(problem.isDead(currchild.state)):
                    curr.child.append(currchild)
                if explored.index(currchild.state) == None:
                    if problem.goalTest(currchild.state):
                        return getSolution(currchild)
                    else:
                        frontier.append(currchild)

