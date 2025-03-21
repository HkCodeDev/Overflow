from a1_partc import Queue
def get_overflow_list(grid):
    """
    Identifies which cells in the grid will overflow.
    A cell overflows if its magnitude(non_negative value, for example if it's -4, its magnitude is 4)
    is greater than or equal to its number of neighbors.
    Returns several (row, col) tuples for the cells that overflow.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    #allocate a list of max size (all cells could overflow)
    overflow_cells = [(None, None)] * (rows * cols)
    count = 0  # Track number of overflow cells
    '''
|-----|-----|-----|-----|-----|
|  C  |  E  |  E  |  E  |  C  |  --> First row (C = Corner, E = Edge)
|-----|-----|-----|-----|-----|
|  E  |  I  |  I  |  I  |  E  |  --> Second row (I = Interior, E = Edge)
|-----|-----|-----|-----|-----|
|  E  |  I  |  I  |  I  |  E  |  --> Third row (I = Interior, E = Edge)
|-----|-----|-----|-----|-----|
|  C  |  E  |  E  |  E  |  C  |  --> Fourth row (C = Corner, E = Edge)
|-----|-----|-----|-----|-----|
'''
    for r in range(rows):
        for c in range(cols):
            # What number of neighbors for cell (r, c)
            #if the cell is in corner:
            #first: check is the cell is top row or bottom row
            #AND
            #second: check if the column is the leftmost or rightmost
            if (r == 0 or r == rows - 1) and (c == 0 or c == cols - 1):
                neighbors = 2  # Corner cells
            #if a cell is in edge
            #check if the cell is in edge but not corner
            #same condition as before except with an "or" instead of "and" to avoid corners
            elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                neighbors = 3  # Edge cells
            #if a cell is interior
            else:
                neighbors = 4  # Interior cells
            
            # absolute value logic
            cell_value = grid[r][c]
            if cell_value < 0:
                cell_value = -cell_value  # Convert "-" to "+"
            
            # If the value of the cell is greater or equal to neighbors, it overflows
            if cell_value >= neighbors:
                overflow_cells[count] = (r, c)
                count += 1
                
    #if there's no overflowing cell:
    if count == 0:
        #return nothing
        return None
    #if there's overflowing cell:
    else:
        #create a new list of size count(the number of overflowing cells)
        result = [(None, None)] * count  
        #iterating over (in number of overflowing size)
        for i in range(count):
            result[i] = overflow_cells[i]  # Copy the overflow cells into the result
        return result


def is_all_positive(grid):
    """
    Checks if all values in the grid are non-negative.
    Returns True if all are >= 0, otherwise False.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < 0:
                return False
    return True

def is_all_negative(grid):
    """
    Checks if all values in the grid are non-positive.
    Returns True if all are <= 0, otherwise False.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                return False
    return True

def apply_overflow(grid, overflow_cells, is_positive_overflow):
    """
    Apply overflow to the grid based on the list of overflowing cells.
    If 'is_positive_overflow' is True, we increase neighboring cells; if False, we decrease them.
    """
    for i, j in overflow_cells:
        grid[i][j] = 0  # Reset the overflowing cell to zero

    for i, j in overflow_cells:
        # Update above neighbor
        if i > 0: #not the first row
            if is_positive_overflow:
                #if it's already positive, keep it that way
                #else: turn it positive
                #then increase it by 1
                grid[i - 1][j] = grid[i - 1][j] if grid[i - 1][j] >= 0 else -grid[i - 1][j]
                grid[i - 1][j] += 1
            else:
                #if it's already negative, keep that way
                #else: turn it negative
                #then decrease it by 1
                grid[i - 1][j] = grid[i - 1][j] if grid[i - 1][j] <= 0 else -grid[i - 1][j]
                grid[i - 1][j] -= 1

        # Update below neighbor
        if i < len(grid) - 1:
            if is_positive_overflow: #make sure the current row is not the last one(out-of-bounds error)
                grid[i + 1][j] = grid[i + 1][j] if grid[i + 1][j] >= 0 else -grid[i + 1][j]
                grid[i + 1][j] += 1
            else:
                grid[i + 1][j] = grid[i + 1][j] if grid[i + 1][j] <= 0 else -grid[i + 1][j]
                grid[i + 1][j] -= 1

        # Update left neighbor
        if j > 0: #not the last column
            if is_positive_overflow:
                grid[i][j - 1] = grid[i][j - 1] if grid[i][j - 1] >= 0 else -grid[i][j - 1]
                grid[i][j - 1] += 1
            else:
                grid[i][j - 1] = grid[i][j - 1] if grid[i][j - 1] <= 0 else -grid[i][j - 1]
                grid[i][j - 1] -= 1

        # Update right neighbor
        if j < len(grid[0]) - 1: #make sure the current cell is not the last column
            if is_positive_overflow:
                grid[i][j + 1] = grid[i][j + 1] if grid[i][j + 1] >= 0 else -grid[i][j + 1]
                grid[i][j + 1] += 1
            else:
                grid[i][j + 1] = grid[i][j + 1] if grid[i][j + 1] <= 0 else -grid[i][j + 1]
                grid[i][j + 1] -= 1

def overflow(grid, a_queue):
    # Step 1: Check if the grid is all non-negative or non-positive
    uniform_grid = is_all_positive(grid) or is_all_negative(grid)
    #if it's uniform (all cell positive or negative):
    #return as it is, without any change
    #Our base case
    if uniform_grid:
        return 0

    # Step 2: Get the list of overflowed cells
    overflow_cells = get_overflow_list(grid)

    # Step 3: If no cells overflow, stop the recursion, return count
    if not overflow_cells:
        return 0

    # Step 4: Determine if the overflow is positive or negative
    #overflow_cells[0][0] and overflow_cells[0][1] are used rather than  overflow_cells[0] 
    #because overflow_cells[0]  shows both row and column but we need both separately to locate the position
    #if it's negative, apply_overflow will make the surrounding cells negative and decrease by 1 in Step 5
    is_positive_overflow = grid[overflow_cells[0][0]][overflow_cells[0][1]] >= 0

    # Step 5: Apply the overflow to the grid
    apply_overflow(grid, overflow_cells, is_positive_overflow)

    # Step 6: Store the current state of the grid in the queue
    # Create an empty 2D list with the same dimensions
    #len(grid): number of rows in the first grid
    #len(grid[0]): number of columns in the first row in first grid
    #for i in range(len(grid)): it iterates through each row, giving columns 0
    current_state = [[0] * len(grid[0]) for i in range(len(grid))]

    # Populate the new 2D list with the values from first grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #copy it to current_state
            current_state[i][j] = grid[i][j]
    a_queue.enqueue(current_state) 

    # Step 7: For next wave of overflow
    #added 1 to count the current wave to be counted
    return 1 + overflow(grid, a_queue)
