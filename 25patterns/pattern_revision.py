#sliding window 
def sliding_window(s->string):
    left = 0 
    win_content={}
    max_score=0
    for right in range(len(s)):
        chara=s[right]
        win_content=win_content.get(chara,0)+1
        while win_content[chara]>1:
            left_char=s[left]
            win_content[left_char]-=1
            if win_content[left_char]==0:
               del win_content[left_char]
            left +=1
        return max(max_score,right-left+1)

#godzilla 
def godzilla(graph):
    if not graph:
        return 0
    rows,cols=len(graph),(graph[0])
    no_of_islands=0
    def dfs_destroyer(r,c):
        #serch # sink # stop # spread
        if r<0 or c < 0 or c>=cols or r>=rows or graph[r][c]=='0':
            return 
        graph[r][c]='0'
        dfs_destroyer[r+1,c]
        dfs_destroyer[r-1,c]
        dfs_destroyer[r,c+1]
        dfs_destroyer[r,c-1]

        for r in range(len(rows)):
            for c in range(len(cols)):
                if graph[r][c]==1:
                    no_of_islands+=1
                    dfs_destroyer(r,c)
    return no_of_islands
                  
def two_pointer(target,s):
    left=0
    right = len(s)-1
    while left<=right:
        sum=s[left]+s[right]
        if sum==target:
            return [left,right]
        if sum < target:
            left +=1
        else :
            right -=1
    return []

#dfs rescursivee 

def dfs(root):
    if not root :
        return 0
    print(root.val)
    left_child = dfs(root.left)
    right_child = dfs(root.right)
    return max(left_child,right_child)+1

from collections import deque
def bfs(root):
    if not root :
        return []
    queue=deque([root])
    result=[]

    while queue:
        curr_size = len(queue)
        curr_result=[]

        for _ in range(curr_size):
            node=queue.popleft()
            curr_result.append(node.val)
            if node.left :
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(curr_result)

    return result

    
#graph bfs practice 
#zombie analogy 
from collections import deque 

def zombie(graph,sr,sc):
    rows,cols=len(graph),len(graph[0])

    queue=deque([(sr,sc,0)])
    visited=set([(sr,sc)])

    compass = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue :
        r,c,day = queue.popleft()
        if graph[sr,sc]=='Target':
            return  day
        for dr ,dc  in compass:
            nr,nc=r+dr,dc+c
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                if graph[nr][nc]!='WALL':
                    visited.add((nr,nc))
                    queue.append((nr,nc,day+1))
    return -1 


        
        
    

