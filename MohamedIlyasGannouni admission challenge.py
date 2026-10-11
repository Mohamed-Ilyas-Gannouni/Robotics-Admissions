def main():

    #The core variables
    x = "walkable" #labels for walkable spaces 
    o = "blocked" #label for blocked spaces
    n = "cube" #Label for the cude
    b = "exit" #Label for exit

    # Situation 1
    
    #Here we are letting the robot grab the cube and try to head towards the exit without any obstacles in its way

    path = [
        [x, x, x, x, x],
        [x, x, x, x, x],
        [x, x, n, x, x],
        [x, x, x, x, x],
        [x, x, x, x, b],
    ] #Here is the 2d matrix representing the gride environment with walkable paths and no blocked paths

    print("Start of Phase 1.")
    cube_l = path_finder(path, n, 0, 0) # Searching for the cube (2,2) starting from the origin (0,0)
    print("Phase 1 done, going to phase 2.")

    print("Start of phase 2.")
    if cube_l: #Only launches the program of Phase 2 if the the program of Phase 1 retrieves the cube
        path_finder(path, b, cube_l[0], cube_l[1]) #Starts from the cube position and searches for the exit
    print("Phase 2 done.")

    #Situation 2

    #Here we are letting the robot grab the cube and try to head towards the exit, however this time there are obstacles in his way
    #Also, note that if the robots finds one way to go to the exit, it will find its way to it (so if we remove one of the three blocks, it will find the exit)

    path = [
            [x, x, x, x, x],
            [x, x, x, x, x],
            [x, x, n, x, x],
            [x, x, x, o, o],
            [x, x, x, o, b],
        ] #Here is the 2d matrix representing the gride environment with walkable paths and blocked paths to stop the robot from going to the exit
    
    print("Start of phase 1.")
    # Searching for the cube (2,2) starting from the origin (0,0)
    cube_l_2 = path_finder(path, n, 0, 0)
    print("Phase 1 done, going to phase 2.")
    
    print("Start of phase 2.")
    if cube_l_2: #Only launches the program of Phase 2 if the the program of Phase 1 retrieves the cube
        path_finder(path, b, cube_l_2[0], cube_l_2[1]) #Starts from the cube position and searches for the exit
    print("Phase 2 done.")



def path_finder(path, target, s_row, s_col): #function that starts a BFS (Breadth First Search) to find its target using the shortest route it can find

        #Activation of memory to track the positions the robot has been to
        visited = [(s_row, s_col)]
        queue = [(s_row, s_col)]

        while queue:
            position = queue.pop(0) # Takes the current position (or extract) from the front of the line
            row = position[0]
            col = position[1]

            #Reads the labels on the grid at current coordinates
            position_num = path[row][col]

            if position_num == target:
                print(f"{target} found")
                return (row, col)

            #This below calculates the coordinates for the 4 squares around 
            around = [
                (row - 1, col), # Up
                (row + 1, col), # Down
                (row, col -1), # Left
                (row, col + 1) #Righ
            ] 

            for r, c in around: # Validate each step
                if 0 <= r <= 4 and 0 <= c <= 4: #Making sure that everything stays in the 5x5 grid (0 to 4)
                    if path[r][c] != "blocked": #Making sure that the square isn't a wall
                        if (r, c) not in visited: #Checking and making sure that the square wasn't visited and analy
                            visited.append((r, c))
                            queue.append((r, c))

        # When the program fails to retrieve the target (cube or exit) it shows and print that message
        print("Failed to find ")
        return None

main()