# Maze Navigation 🏃

![demo](https://user-images.githubusercontent.com/63660298/171042477-b9879d25-4889-40aa-994f-77dcf387b682.png)

# Introduction 📝

Maze navigation, also known as path planning, is essential for autonomous mobile robots. It allows them to find the best route between two points. In this project, we will attempt to develop four search algorithms in [Python3](www.python.org) which are Birth First search, Depth-first search, Greedy, and A*.

# Algorithms ✨

## 1. Birth First search (BFS)
Bith-first search is an algorithm that starts at the starting point and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. [Read More](https://en.wikipedia.org/wiki/Breadth-first_search)

## 2. Depth First Search (DFS)
Depth First search is an algorithm that starts from the starting point and explore the path as far as possible from that starting point. We will find that this algorithm is always bad for this problem.

## 3. Greedy
A greedy algorithm is an algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. [Read More](https://en.wikipedia.org/wiki/Greedy_algorithm)

## 4. A*
A* is an efficient informed algorithm that avoids expanding the expensive solution by using the heuristic function to estimate the cost. The heuristic function is essentially a euclidean distance computation from the current position to the goal position, allowing us to identify the quickest path possible.

## Installation 📑
In order to run this project, you must have [Python3](https://www.python.org/) installed on your machine. You also must have all listed libraries inside the `requirments.txt` so run the following command to install them: 
```
pip3 install -r requirments.txt
```

## Running instructions
In order to run the program, you must have a black and white maze image saved in samples. You can re-use the demo.png, but also feel free to use or draw one on your own. Run `Python3 Maze.py` and follow the instructions. Note that the solution will be generated in the samples folder at the end

![image](https://user-images.githubusercontent.com/63660298/171045848-b0a4ee89-b14d-46c2-8843-5d5cb7c2755c.png)


# Sample run 🏃

* Initial state of a random maze

![demo](https://user-images.githubusercontent.com/63660298/171044796-125b3b22-8fa1-4530-b647-702cc4c3747d.png)

* Result after running A* on the maze

![demo_result](https://user-images.githubusercontent.com/63660298/171044844-ce2429ae-7c97-45a5-9168-06d23dc7b8b7.png)


# Files 🗃️

```
.
├── README.md
└── src
    ├── Maze.py               | The main
    ├── PriorityQueue.py      | Priority Queue Data Structure
    ├── Queue.py              | Queue Data Structure
    ├── samples               | Samples folder
    │   ├── demo.png
    │   └── demo_result.png
    ├── Requirments.txt       | Required python libraries
    ├── Stack.py              | Stack Data Structure
    └── Tree.py               | Tree Data Structure
```

# Conclusion 😊
In this project, We implemented four searching algorithms to find the path from the starting point to the goal location. This project was created to discover the differences between the four algorithms, therefore feel free to try all of them to have a better understanding of how each algorithm works. Please keep in mind that the project code was not perfect, therefore feel free to fork this repository and enhance it.

