from collections import deque
#@author Dhruv
#bfs pattern
def levelOrder(root):
    if not root:
        return []
        
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_floor = []
        
        # Process ONLY the people currently on this floor
        for _ in range(level_size):
            node = queue.popleft()
            current_floor.append(node.val)
            
            # Send the subordinates to the back of the line
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_floor)
        
    return result
#Memorization Trick 
"""
🧠 The OA "Sniper" Thought Process (Line-by-Line)You are in the OA. The clock is at 35:00. The question is "Binary Tree Level Order Traversal."1. "Check for an empty building."Python    if not root:
        return []
Thought Process: "If they pass me a None tree, the building is empty. Hand back an empty list and move on."2. "Set up the waiting line and the final report."Python    queue = deque([root])
    result = []
Thought Process: "I need a fast double-ended queue (deque) so I can pop from the front in $O(1)$ time. I put the root (the CEO) in the line first. result is my final answer sheet to hand to the interviewer."3. "Keep exploring as long as there is a line."Python    while queue:
        level_size = len(queue)
        current_floor = []
Thought Process: "The while loop runs as long as the building has people. But here is the critical trick: I MUST take a snapshot of len(queue) right now. If I don't lock in this level_size, I will accidentally start processing the next floor's kids while I'm still on the current floor!"4. "Clear the current floor."Python        for _ in range(level_size):
            node = queue.popleft()
            current_floor.append(node.val)
Thought Process: "I loop exactly level_size times. I pop the guy at the front of the line, and I write his name (node.val) down on my current_floor clipboard."5. "Queue up the next generation."Python            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
Thought Process: "I am standing with this node. I look to his left and right. If he has kids (children nodes), I tell them, 'Go get in the back of the queue.' They won't be processed in this for loop because I already locked in the level_size earlier!"6. "File the paperwork."Python        result.append(current_floor)
Thought Process: "The for loop finished. The current floor is completely processed. I staple the current_floor clipboard into my main result folder. The while loop restarts for the next floor."
"""