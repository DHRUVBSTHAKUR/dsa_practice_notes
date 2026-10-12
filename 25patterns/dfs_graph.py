#godzilla code
#best memory trick 
#@author Dhruv 

def numIslands(grid):
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    islands_destroyed = 0
    
    def destroy_island(r, c):
        # S.S.S.S - Step 2: STOP
        # Stop if out of bounds (off the map) OR if it's water (nothing to destroy)
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # S.S.S.S - Step 3: SINK
        # Turn land to water so we don't visit it again
        grid[r][c] = '0' 
        
        # S.S.S.S - Step 4: SPREAD
        # Spread the destruction to neighbors
        destroy_island(r+1, c)
        destroy_island(r-1, c)
        destroy_island(r, c+1)
        destroy_island(r, c-1)

    # S.S.S.S - Step 1: SCAN
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':     # Found a new island
                islands_destroyed += 1 # Count it
                destroy_island(r, c)   # Wipe it off the map
                
    return islands_destroyed

"""
The Mental Model: "Destroy the Island"
Imagine you are a giant monster (Godzilla) wading through the ocean. You are counting how many islands exist.

You scan the map grid by grid.

The moment you step on land ('1'), you shout "ONE!" (increment count).

Crucial Step: To make sure you don't count this same island again later, you sink the entire island into the ocean immediately. You stomp on the spot you found, and then run to every connected piece of land and stomp on it too until the whole island is gone (turned to '0').

You return to your scan. Since that island is now water ('0'), you will never count it again.

The 4-Step Mnemonic: S.S.S.S.
To write the code, just remember S.S.S.S.

Scan (The nested loops)

Stop (The DFS base case)

Sink (Mark as visited)

Spread (The recursive calls)

1. SCAN (The Loops)
You need to look at every cell to find the islands.

Logic: Iterate through every row and column.

Trigger: If you see a '1', that's a new island. Increment count and launch the attack (DFS).

Python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '1':  # Found land!
            count += 1         # Count it
            dfs(r, c)          # DESTROY the rest of this island
2. STOP (DFS Base Case)
When does the destruction stop?

Logic: You stop if you run off the edge of the map OR if you hit water (because there is nothing to destroy).

Code:

Python
if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
    return
3. SINK (The Mutation)
This is the secret sauce. You must change the '1' to a '0'.

Why? If you don't turn it to 0, your code will infinitely loop between two cells, or you will recount this piece of land later in your main loop.

Code: grid[r][c] = '0'

4. SPREAD (Recursion)
The fire spreads in all 4 cardinal directions.

Logic: Up, Down, Left, Right.

Code: dfs(r+1, c), dfs(r-1, c), etc.

Visualizing the "Sink"
If the input is this:

Plaintext
1 1 0
1 0 0
0 0 1
Loop finds grid[0][0] is 1. Count = 1.

DFS triggers. It sinks (0,0), then spreads to (0,1) and (1,0). It turns them ALL to 0.

The grid is now:

Plaintext
0 0 0
0 0 0
0 0 1
Loop continues. It skips everything until it hits grid[2][2].

It sees a 1. Count = 2. DFS triggers and sinks it.

The "Godzilla" Annotated Code
Read this version. It uses the mental model as comments.


Next Step for You
To lock this in, don't just read it. Go to LeetCode right now and try to solve "Max Area of Island". It uses the exact same pattern (S.S.S.S.), but instead of just sinking, you return 1 + sum of neighbors to get the size.

"""

"""
SSSS
SCAN 
for r in ranag(grid):
    for c in range(grid):
        if grid[][]==1:
            count+=1
            dfs(r,c)
stop 
if r<0 or c < 0 or r >=rows or c>=cols or grid[0][0]:
    return 

SINK 
grid[r][c]==0
SPREAD 
dfs(r+1,c)
dfs(r-1,c)
dfs(r,c+1)
dfs(r,c-1)
"""
