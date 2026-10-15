from collections import deque

def shortest_path(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    
    # 1. The Setup 
    queue = deque([(start_r, start_c, 0)])  # (row, col, distance)
    visited = set([(start_r, start_c)])
    
    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    # 2. The Infection Loop
    while queue:
        r, c, dist = queue.popleft()
        
        # Did we reach the target?
        if grid[r][c] == 'TARGET':
            return dist
            
        # 3. Look in all 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 4. The Safety Check (Bounds and Visited)
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 'WALL':  # Is it a valid path?
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
    return -1 # Target not reachable