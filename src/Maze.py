import sys
import os
import time
from PIL import Image
from Queue import Queue
from PriorityQueue import PriorityQueue
from Stack import Stack
from Tree import Tree, Node


class Maze:
    def __init__(self):
        self.initial_state = None
        self.cordinates = {"initial": None, "goal": None}
        self.filename = None
        self.algorithm = None
        self.type = 0
        self.image = None
        self.expanded_nodes = 0
        self.frontier_maximum = 0
        self.path_cost = 0

    # helper function: to determind the color if it is close to white or black
    def close_to(self, pixle: tuple):
        return "0" if(sum(pixle) > 390) else "1"

    # read the input as PNG extension:
    def read_input(self, file):
        self.filename = file.replace(".png", "")
        self.image = Image.open(os.path.join(sys.path[0], "inputs", file))
        self.image = self.image.convert(mode="RGB")
        pixels = list(self.image.getdata())
        width, height = self.image.size
        pixels = [pixels[x*width:(x+1)*width] for x in range(height)]
        self.initial_state = [
            [self.close_to(pixle) for pixle in row] for row in pixels]
        return (self.filename, self.image.size)

    # write the output as PNG and GIF extensions
    def write_output(self, solution, gif=0):
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 10, 255)
        cyan = (0, 255, 255)
        visited = list((solution[1]))
        path = self.get_path(solution[0])
        pixels = self.image.load()
        initial = self.cordinates["initial"]
        goal = self.cordinates["goal"]
        pixels[initial[1], initial[0]] = red
        pixels[goal[1], goal[0]] = green
        if(gif):
            frames = []
            for position in visited[1:]:
                if(position != initial and position != goal):
                    pixels[position[1], position[0]] = cyan
                    temp = self.image.copy()
                    frames.append(temp)
            for position in path:
                pixels[position[1], position[0]] = blue
                temp = self.image.copy()
                frames.append(temp)
            frames[0].save('outputs/{}.gif'.format(self.filename),
                           append_images=frames[1:], save_all=True, duration=20, loop=0)
        else:
            for position in visited[1:]:
                if(position != initial and position != goal):
                    pixels[position[1], position[0]] = cyan
            for position in path:
                pixels[position[1], position[0]] = blue
        self.image.save("outputs/{}.png".format(self.filename))

    # helper function: check the new position if it is valid for the movement function
    def check_position(self, state, new_position):
        x, y = new_position[0], new_position[1]
        if(state[x][y] == '1'):
            return None
        return new_position

    # movements: to find all the possible moves
    def movements(self, position):
        state = self.initial_state
        new_states = []
        max_x, max_y = len(state), len(state[0])
        x, y = position[0], position[1]

        if(x-1 >= 0):
            new_state = self.check_position(state, [x-1, y])
            if(new_state):
                new_states.append([x-1, y])

        if(x+1 < max_x):
            new_state = self.check_position(state, [x+1, y])
            if(new_state):
                new_states.append([x+1, y])

        if(y-1 >= 0):
            new_state = self.check_position(state, [x, y-1])
            if(new_state):
                new_states.append([x, y-1])

        if(y+1 < max_y):
            new_state = self.check_position(state, [x, y+1])
            if(new_state):
                new_states.append([x, y+1])

        if(x-1 >= 0 and y+1 < max_y and state[x-1][y] != "1" and state[x][y+1] != "1"):
            new_state = self.check_position(state, [x-1, y+1])
            if(new_state):
                new_states.append([x-1, y+1])

        if(x-1 >= 0 and y-1 >= 0 and state[x-1][y] != "1" and state[x][y-1] != "1"):
            new_state = self.check_position(state, [x-1, y-1])
            if(new_state):
                new_states.append([x-1, y-1])

        if(x+1 < max_x and y+1 < max_y and state[x+1][y] != "1" and state[x][y+1] != "1"):
            new_state = self.check_position(state, [x+1, y+1])
            if(new_state):
                new_states.append([x+1, y+1])

        if(x+1 < max_x and y-1 >= 0 and state[x+1][y] != "1" and state[x][y-1] != "1"):
            new_state = self.check_position(state, [x+1, y-1])
            if(new_state):
                new_states.append([x+1, y-1])

        return new_states

    # get_path: to get the solution path
    def get_path(self, state):
        path = []
        while(state != None):
            path.append(state.position)
            state = state.parent
        self.path_cost = len(path)
        return path

    # Estimated cost for Greedy and A*
    def estimated_cost(self, position):
        if(self.type == 1):
            goal = self.cordinates["goal"]
            estimated_cost = abs(
                position[0]-goal[0]) + abs(position[1]-goal[1])
            return estimated_cost
        elif(self.type == 2):
            goal = self.cordinates["goal"]
            estimated_cost = pow(
                position[0]-goal[0], 2) + pow(position[1]-goal[1], 2)
            estimated_cost = pow(estimated_cost, 0.5)
            return estimated_cost

    # Bredth first search (BFS)
    def BFS(self):
        BFS_tree = Tree(self.cordinates["initial"], False)
        frontier = Queue()
        frontier.enqueue(BFS_tree.root)
        visited = set()
        pixels = []
        while(frontier.size != 0):
            current_state = frontier.pop()
            adj = self.movements(current_state.position)
            visited.add((current_state.position[0], current_state.position[1]))
            pixels.append(current_state.position)
            for state in adj.copy():
                if((state[0], state[1]) not in visited):
                    adj_node = Node(state, parent=current_state)
                    current_state.adj.append(adj_node)
                    frontier.enqueue(adj_node)
                    if(frontier.size > self.frontier_maximum):
                        self.frontier_maximum = frontier.size
                    visited.add((state[0], state[1]))
                    pixels.append(state)
                    if(state == self.cordinates["goal"]):
                        self.expanded_nodes = len(visited)
                        return(current_state, pixels)
        return None

    # Depth first search (DFS):
    def DFS(self):
        DFS_tree = Tree(self.cordinates["initial"], False)
        frontier = Stack()
        frontier.push(DFS_tree.root)
        visited = set()
        pixels = []
        while(frontier.size != 0):
            current_state = frontier.pop()
            adj = self.movements(current_state.position)
            visited.add((current_state.position[0], current_state.position[1]))
            pixels.append(current_state.position)
            for state in adj.copy():
                if((state[0], state[1]) not in visited):
                    adj_node = Node(state, parent=current_state)
                    current_state.adj.append(adj_node)
                    frontier.push(adj_node)
                    if(frontier.size > self.frontier_maximum):
                        self.frontier_maximum = frontier.size
                    visited.add((state[0], state[1]))
                    pixels.append(state)
                    if(state == self.cordinates["goal"]):
                        self.expanded_nodes = len(visited)
                        return(current_state, pixels)
        return None

    # Greedy Best-first search:
    def Greedy(self):
        Greedy_tree = Tree(self.cordinates["initial"], False)
        frontier = PriorityQueue()
        frontier.enqueue(Greedy_tree.root)
        visited = set()
        pixels = []
        while(frontier.size != 0):
            current_state = frontier.pop()
            adj = self.movements(current_state.position)
            visited.add((current_state.position[0], current_state.position[1]))
            pixels.append(current_state.position)
            for state in adj.copy():
                if((state[0], state[1]) not in visited):
                    estimated_cost = self.estimated_cost(state)
                    adj_node = Node(state, cost=estimated_cost,
                                    parent=current_state)
                    current_state.adj.append(adj_node)
                    frontier.enqueue(adj_node)
                    if(frontier.size > self.frontier_maximum):
                        self.frontier_maximum = frontier.size
                    visited.add((state[0], state[1]))
                    pixels.append(state)
                    if(state == self.cordinates["goal"]):
                        self.expanded_nodes = len(visited)
                        return(current_state, pixels)
        return None

    # A*:
    def A(self):
        A_tree = Tree(self.cordinates["initial"], False)
        frontier = PriorityQueue()
        frontier.enqueue(A_tree.root)
        visited = set()
        pixels = []
        while(frontier.size != 0):
            current_state = frontier.pop()
            adj = self.movements(current_state.position)
            visited.add((current_state.position[0], current_state.position[1]))
            pixels.append(current_state.position)
            for state in adj.copy():
                if((state[0], state[1]) not in visited):
                    estimated_cost = self.estimated_cost(
                        state) + current_state.depth + 1
                    adj_node = Node(state, cost=estimated_cost,
                                    parent=current_state)
                    current_state.adj.append(adj_node)
                    frontier.enqueue(adj_node)
                    if(frontier.size > self.frontier_maximum):
                        self.frontier_maximum = frontier.size
                    visited.add((state[0], state[1]))
                    pixels.append(state)
                    if(state == self.cordinates["goal"]):
                        self.expanded_nodes = len(visited)
                        return(current_state, pixels)
        return None

    # Main Function to run the program

    def main(self):
        while(True):
            print("Write the file name:")
            print(os.listdir(os.path.join(sys.path[0], "inputs")))
            filename = input()
            if(filename not in os.listdir(os.path.join(sys.path[0], "inputs"))):
                print("The file is not exist.")
                continue
            reader = self.read_input(filename)
            print("Opening: ", reader[0], " Size:", reader[1])

            width, height = reader[1][0], reader[1][1]

            initial = []
            print("Enter the x of the starting point:")
            initial.insert(0, int(input()))
            print("Enter the y of the starting point: ")
            initial.insert(0, int(input()))
            self.cordinates["initial"] = initial

            goal = []
            print("Enter the x of the goal point:")
            goal.insert(0, int(input()))
            print("Enter the y of the goal point: ")
            goal.insert(0, int(input()))
            self.cordinates["goal"] = goal

            print(self.cordinates)

            if(initial[0] >= height or initial[0] < 0 or initial[1] >= height or initial[1] < 0 or
                    goal[0] >= width or goal[0] < 0 or goal[1] >= width or goal[1] < 0):
                print(
                    "Please Enter a valid numbers. One or all of the number you  have entered are out of bound.")
                continue
            elif(self.initial_state[initial[0]][initial[1]] == "1" or self.initial_state[goal[0]][goal[1]] == "1"):
                print("One of these points is an obstacle.")
                continue
            elif(initial == goal):
                print("The initial and goal state cannot be the same.")
                continue

            print("Choose an algorithm:")
            print("[1] Bredth first search (BFS)")
            print("[2] Depth first search  (DFS)")
            print("[3] Greedy Best-first search")
            print("[4] A*")

            algorithm = int(input())

            if(algorithm == 3 or algorithm == 4):
                print(
                    "Choose [1] Euclidean distance or [2] Manhattan distance")
                self.type = int(input())
                if(self.type != 1 and self.type != 2):
                    print("Please choose a valid number")
                    continue

            start_time = time.time()
            if(algorithm == 1):
                print("Started solving the maze using BFS algorithm")
                solution = self.BFS()
            elif(algorithm == 2):
                print("Started solving the maze using DFS algorithm")
                solution = self.DFS()
            elif(algorithm == 3):
                print("Started solving the maze using Greedy algorithm")
                solution = self.Greedy()
            elif(algorithm == 4):
                print("Started solving the maze using A* algorithm")
                solution = self.A()
            end_time = time.time()

            if(not solution):
                print("The program could not find the path.")
                break

            print(round((end_time - start_time), 5), "Seconds")

            print("Do you want to extract a gif solution? (y/n)")
            gif = input()
            if(gif == "y"):
                self.write_output(solution, gif=1)
            else:
                self.write_output(solution)

            print("Count of expanded nodes: ", self.expanded_nodes)
            print("Path cost: ", self.path_cost)
            print("frontier maximum: ", self.frontier_maximum)

            print("The solution has been written.")
            break


if __name__ == '__main__':
    game = Maze()
    game.main()
