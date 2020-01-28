# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """
    While the current position is not the goal position,
        put the current position to the the exploredPositions
        get the successors of the current position,
        if there are not any successors and the Fringe is empty return there isnt any solution
        set the first successor as the currentState
        set the current position to currentState[0]
        and add the action to get to the new postition to the listOfActions
        if the new position is the goal return the listOfActions
        put the remaining successors in the Fringe list along with the actions required
        to get to these states Fringe = [((state),[listOfActions required to get to the parent state])]

        if the current position is in the exploredPositions:
                set the current state to fringe[0][0]
                set the current position to currentState[0]
                set the listOfActions to currentState[1]

    """

    listOfActions = []
    currentPacmanPosition = problem.getStartState()

    Fringe = []
    exploredPositions = []
    count = 0

    while not problem.isGoalState(currentPacmanPosition):
        exploredPositions.append(currentPacmanPosition)
        successors = problem.getSuccessors(currentPacmanPosition)

        if len(successors) == 0 and len(Fringe) == 0:
                return listOfActions #Which should be empty

        for index, item in enumerate(successors):
            if item[0] not in exploredPositions:
                currentState = item
                break
            elif index == len(successors):
                    if len(Fringe) != 0:
                        NewStateWithActions = Fringe.pop(0)
                        currentState = NewStateWithActions[0]
                    else:
                        print("There is no Fringe left and all the successors have been explored")
                        return None

        currentPacmanPosition = currentState[0]
        listOfActions.append(currentState[1])

        if  problem.isGoalState(currentPacmanPosition):
            return listOfActions

        Fringe = [[x, listOfActions[:-1] + [x[1]]] for x in successors[1:] if x[0] not in exploredPositions] + Fringe # [(state),list of actions to get to that state]

        if currentPacmanPosition in exploredPositions:
            NewStateWithActions = Fringe.pop(0)
            currentState = NewStateWithActions[0]
            currentPacmanPosition = currentState[0]
            listOfActions = NewStateWithActions[1]

        count += 1
        """
        if count == 18:
            print(listOfActions)
            print(exploredPositions)
            print(Fringe)
            print(currentPacmanPosition)

            return None
        """
            #print("the new pacman position is: {}".format(currentPacmanPosition))
            #print("the fringe is: {}".format(Fringe))
    #print(count)
    print(currentPacmanPosition)

    return listOfActions



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
