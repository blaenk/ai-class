# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

from sets import Set
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    visited = Set([])
    path = []
    visit = util.Stack()

    root = problem.getStartState()

    # populate the fringe with preliminary children
    for successor in problem.getSuccessors(root):
      visit.push(successor)

    visit.push(True) # denote new level

    while not visit.isEmpty():
      while True:
        # check next node
        next_node = visit.pop()

        # if the node is 'True' then it means we went back a level
        if next_node == True:
          # so delete an action from the path
          if path:
            path.pop()
        # otherwise check if this is a state we haven't seen before
        else:
          current_state = next_node[0]
          action_to = next_node[1]

          if current_state not in visited:
            break

      visited.add(current_state) # add state to set
      path.append(action_to) # add action to path

      # check win state
      if problem.isGoalState(current_state):
        return path

      visit.push(True) # denote new level

      # push the next level of children
      for successor in problem.getSuccessors(current_state):
        visit.push(successor)

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    visited = Set([])
    path = []
    visit = util.Queue()

    root = problem.getStartState()

    # populate the fringe with preliminary children
    for successor in problem.getSuccessors(root):
      visit.push([successor])

    while not visit.isEmpty():
      while True:
        # check next node
        next_path = visit.pop()
        next_node = next_path[-1]

        current_state = next_node[0]

        if current_state not in visited:
          break

      visited.add(current_state) # add state to set

      # check win state
      if problem.isGoalState(current_state):
        return map(lambda node: node[1], next_path)

      for successor in problem.getSuccessors(current_state):
        new_path = list(next_path)
        new_path.append(successor)
        visit.push(new_path)

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visited = Set([])
    path = []
    visit = util.PriorityQueue()

    root = problem.getStartState()

    # populate the fringe with preliminary children
    for successor in problem.getSuccessors(root):
      visit.push([successor], problem.getCostOfActions([successor[1]]))

    while not visit.isEmpty():
      while True:
        # check next node
        next_path = visit.pop()
        next_node = next_path[-1]

        current_state = next_node[0]

        if current_state not in visited:
          break

      visited.add(current_state) # add state to set

      # check win state
      if problem.isGoalState(current_state):
        return map(lambda node: node[1], next_path)

      for successor in problem.getSuccessors(current_state):
        new_path = list(next_path)
        new_path.append(successor)

        actions = map(lambda node: node[1], new_path)
        visit.push(new_path, problem.getCostOfActions(actions))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visited = Set([])
    path = []
    visit = util.PriorityQueue()

    root = problem.getStartState()

    # populate the fringe with preliminary children
    # state, action, cost
    for successor in problem.getSuccessors(root):
      visit.push([successor], problem.getCostOfActions([successor[1]]) + heuristic(successor[0], problem))

    while not visit.isEmpty():
      while True:
        # check next node
        next_path = visit.pop()
        next_node = next_path[-1]

        current_state = next_node[0]

        if current_state not in visited:
          break

      visited.add(current_state) # add state to set

      # check win state
      if problem.isGoalState(current_state):
        return map(lambda node: node[1], next_path)

      for successor in problem.getSuccessors(current_state):
        new_path = list(next_path)
        new_path.append(successor)
        actions = map(lambda node: node[1], new_path)
        visit.push(new_path, problem.getCostOfActions(actions) + heuristic(successor[0], problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
