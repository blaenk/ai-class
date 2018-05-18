# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()
    legalMoves.remove(Directions.STOP)

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    score = successorGameState.getScore()

    # distance to closest food
    from util import manhattanDistance
    
    if newFood.asList():
      score += 1.0 / min(map(lambda foodPos: manhattanDistance(foodPos, newPos), newFood.asList()))

    return score

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    def maxvalue(state, depth, agent):
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      successors = [state.generateSuccessor(agent, action) for action in legalActions]
      values = map(lambda state: value(state, depth, agent + 1), successors)

      actionScores = zip(legalActions, values)
      best = max(actionScores, key=lambda pair: pair[1])

      if depth == 0:
        self.bestAction = best[0]

      return best[1]

    def minvalue(state, depth, agent):
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      successors = [state.generateSuccessor(agent, action) for action in legalActions]
      values = map(lambda state: value(state, depth, agent + 1), successors)

      return min(values)

    def value(state, depth, agent):
      if agent == state.getNumAgents():
        agent = 0
        depth += 1

      if depth == self.depth or state.isWin() or state.isLose():
        return self.evaluationFunction(state)

      if agent == 0:
        return maxvalue(state, depth, agent)
      else:
        return minvalue(state, depth, agent)

    val = value(gameState, 0, 0)
    print val
    return self.bestAction

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    def maxvalue(state, depth, agent, alpha, beta):
      v = float("-inf")
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      for action in legalActions:
        successor = state.generateSuccessor(agent, action)

        val = value(successor, depth, agent + 1, alpha, beta)

        if val > v:
          v = val

          if depth == 0:
            self.bestAction = action

        if v >= beta:
          return v

        alpha = max(alpha, v)

      return v

    def minvalue(state, depth, agent, alpha, beta):
      v = float("inf")
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      for action in legalActions:
        successor = state.generateSuccessor(agent, action)
        v = min(v, value(successor, depth, agent + 1, alpha, beta))

        if v <= alpha:
          return v

        beta = min(beta, v)

      return v

    def value(state, depth, agent, alpha, beta):
      if agent == state.getNumAgents():
        agent = 0
        depth += 1

      if depth == self.depth or state.isWin() or state.isLose():
        return self.evaluationFunction(state)

      if agent == 0:
        return maxvalue(state, depth, agent, alpha, beta)
      else:
        return minvalue(state, depth, agent, alpha, beta)

    val = value(gameState, 0, 0, float("-inf"), float("inf"))
    print val
    return self.bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    def maxvalue(state, depth, agent):
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      successors = [state.generateSuccessor(agent, action) for action in legalActions]
      values = map(lambda state: value(state, depth, agent + 1), successors)

      actionScores = zip(legalActions, values)
      best = max(actionScores, key=lambda pair: pair[1])

      if depth == 0:
        self.bestAction = best[0]

      return best[1]

    def expectivalue(state, depth, agent):
      legalActions = state.getLegalActions(agent)

      if Directions.STOP in legalActions:
        legalActions.remove(Directions.STOP)

      successors = [state.generateSuccessor(agent, action) for action in legalActions]
      values = map(lambda state: value(state, depth, agent + 1), successors)

      avg = sum(values)/len(values)

      return avg

    def value(state, depth, agent):
      if agent == state.getNumAgents():
        agent = 0
        depth += 1

      if depth == self.depth or state.isWin() or state.isLose():
        return self.evaluationFunction(state)

      if agent == 0:
        return maxvalue(state, depth, agent)
      else:
        return expectivalue(state, depth, agent)

    val = value(gameState, 0, 0)
    print val
    return self.bestAction

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    I just did the simplest thing I could. I copied the solution from Question 1 above (ReflexAgent),
    to simply serve as a starting point. My solution simply adds the reciprocal of the distance
    to the closest food. I then ran it to make sure everything was all good, and it did surprisingly well,
    so I left it this way.
  """

  "*** YOUR CODE HERE ***"
  newPos = currentGameState.getPacmanPosition()
  newFood = currentGameState.getFood()
  newGhostStates = currentGameState.getGhostStates()
  newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
  score = currentGameState.getScore()

  # distance to closest food
  
  if newFood.asList():
    score += 1.0 / min(map(lambda foodPos: manhattanDistance(foodPos, newPos), newFood.asList()))

  return score

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

