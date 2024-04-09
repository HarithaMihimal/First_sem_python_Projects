try: 

    def traverse(Start, End, Maze, STACK=None, traversed_cells=set()): # deffine the function for etarate maze

        if STACK is None: # checkup
            STACK = [Start]
            traversed_cells.add(Start) # update the set

        current_cell = STACK[-1]

        if current_cell == End: # checkup
            print("Leaving at ( %d , %d )"%(current_cell[0],current_cell[1]))

            return True, STACK

        instant_string = Maze[current_cell[0]][current_cell[1]] # creating small string using the values of inside the maze

        for char in instant_string:
            cell_new = None

            if char == "U": # checkup
                cell_new = (current_cell[0] - 1, current_cell[1])
                if cell_new not in traversed_cells:
                    print("North ",end="")

            elif char == "L": # checkup
                cell_new = (current_cell[0], current_cell[1] - 1)
                if cell_new not in traversed_cells:
                    print("West ",end="")

            elif char == "D": # checkup
                cell_new = (current_cell[0] + 1, current_cell[1])
                if cell_new not in traversed_cells:
                    print("South ",end="")
            elif char == "R": # checkup
                cell_new = (current_cell[0], current_cell[1] + 1)
                if cell_new not in traversed_cells:
                    print("East ",end="")


            if cell_new not in traversed_cells: #checking  stored value not in the set
                traversed_cells.add(cell_new)
                STACK.append(cell_new)
                result = traverse(Start, End, Maze, STACK, traversed_cells) # recall the function

                if result[0]:
                    return True, STACK
                print("Back to ( %d , %d )"%(current_cell[0],current_cell[1]))

                STACK.pop()
        print("Stuck at ( %d , %d )"%(current_cell[0],current_cell[1]))

        return False, STACK

   # creating maze according to the given question
    # maze as 2D list
    maze_data = [
        ['RD', 'RL', 'RDL', 'L', 'RD', 'RL', 'DL', 'R', 'RDL', 'RL', 'L', 'RD', 'RL', 'DL'],
        ['UD', 'R', 'URL', 'L', 'UD', 'R', 'URDL', 'RDL', 'UDL', 'R', 'RL', 'URL', 'L', 'UD'],
        ['URL', 'RDL', 'L', 'RD', 'UL','RD', 'L', 'UD', 'UR', 'RL', 'RL', 'DL', 'RD', 'UDL'],
        ['UD', 'UD', 'RD', 'URDL', 'RL', 'UL', 'R', 'URL', 'L', 'RD', 'RL', 'UL', 'UD', 'UD'],
        ['UD', 'UD', 'UD', 'UD', 'RD', 'RL', 'RL', 'DL', 'RD', 'UL', 'RD', 'RL', 'UL', 'UD'],
        ['UD', 'UD', 'U', 'UD', 'UD', 'RD', 'L', 'UD', 'UD', 'RD', 'UDL', 'RD', 'DL', 'U'],
        ['U', 'URD', 'DL', 'UD', 'UD', 'UD', 'RD', 'UDL', 'UL', 'UD', 'UD', 'UD', 'UD', 'D'],
        ['D', 'UD', 'UD', 'UD', 'UD', 'UD', 'URD', 'L', 'D', 'U', 'URD', 'UL', 'UD', 'UD'],
        ['UD', 'U', 'URD', 'UL', 'UD', 'UR', 'UL', 'RD', 'UL', 'D', 'UD', 'RD', 'URL', 'UDL'],
        ['URD', 'RL', 'URL', 'L', 'UR', 'RL', 'DL', 'UR', 'RL', 'URL', 'UDL', 'UD', 'D', 'UD'],
        ['U', 'D', 'RD', 'RL', 'RL', 'DL', 'URD', 'DL', 'RD', 'RL', 'UL', 'UD', 'UD', 'UD'],
        ['RD', 'UDL', 'UD', 'RD', 'DL', 'UR', 'UL', 'UD', 'UR', 'RL', 'DL', 'UD', 'UR', 'UL'],
        ['UD', 'UR', 'UL', 'UD', 'UR', 'RDL', 'L', 'U', 'RD', 'RL', 'UL', 'UR', 'L', 'D'],
        ['UR', 'RL', 'RL', 'URL', 'L', 'UR', 'RL', 'RL', 'URL', 'RL', 'RL', 'RL', 'RL', 'UL']
    ]


    start_pos = (2, 0) # giving starting possition in maze
    end_pos = (11, 13) # giving ending possition in maze
    print("Start at ( %d , %d )"%(start_pos[0],start_pos[1])) # print first output
    STACK = traverse(start_pos, end_pos, maze_data) # call traverse_maze function and store values

except:
    pass
