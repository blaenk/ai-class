Projects for UC Berkeley's [CS 188 - Intro to AI](http://ai.berkeley.edu/home.html) offered on edX as [CS 188x](https://courses.edx.org/courses/BerkeleyX/CS188x_1/1T2013/course/) in the Fall of 2012.

1. [Search](/search/)

    Implement search agents using [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search), [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search), [Uniform Cost Search](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs), and [A* Search](https://en.wikipedia.org/wiki/A*_search_algorithm).

    See:

    * [commands.txt](/search/commands.txt): valid run commands
    * [search.py](/search/search.py): search algorithms
    * [searchAgents.py](/search/searchAgents.py): search-based agents

2. [Multi-Agent Pacman](/multi-agent-search/)

    Implement [Minimax](https://en.wikipedia.org/wiki/Minimax) and [Expectimax](https://en.wikipedia.org/wiki/Expectiminimax_tree) search agents.

    See:
    
    * [commands.txt](/multi-agent-search/commands.txt): valid run commands
    * [multiAgents.py](/multi-agent-search/multiAgents.py): multi-agent search agents
    * [pacman.py](/multi-agent-search/pacman.py): runs Pacman, describes `GameState`
    * [game.py](/multi-agent-search/game.py): Pacman logic, describes `AgentState`, `Agent`, `Direction`, `Grid`
    * [util.py](/multi-agent-search/util.py): search algorithm data structures

3. [Reinforcement Learning](/reinforcement-learning/)

    Implement [Markov Decision Processes](https://en.wikipedia.org/wiki/Markov_decision_process): [value iteration](https://en.wikipedia.org/wiki/Markov_decision_process#Value_iteration) and [Q-learning](https://en.wikipedia.org/wiki/Q-learning).

    See:
    
    * [commands.txt](/reinforcement-learning/commands.txt): valid run commands
    * [valueIterationAgents.py](/reinforcement-learning/valueIterationAgents.py): value iteration agent for solving known Markov Decision Processes
    * [qlearningAgents.py](/reinforcement-learning/qlearningAgents.py): Q-learning agents for `Gridworld`, `Crawler`, and `Pacman`
    * [analysis.py](/reinforcement-learning/analysis.py): answers to project questions