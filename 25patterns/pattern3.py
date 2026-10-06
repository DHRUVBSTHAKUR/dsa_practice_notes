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

#Common doubts 
"""
Bro, it is totally normal to have this doubt. It feels like extra steps for no reason, right? Why build a small list just to shove it into a bigger list?

Here is the exact reason: It is because of what the interviewer (or the LeetCode compiler) explicitly asks you to return.

They don't just want to know who is in the building. They want to know exactly what floor everyone is on.

📝 The Difference in Output
Let's say our tree looks like this:

Floor 1: [CEO]

Floor 2: [Manager A, Manager B]

Floor 3: [Intern X, Intern Y, Intern Z]

Scenario A: Using only ONE list (No current_floor)
If you just do result.append(node.val) as you pop people out of the queue, your final answer looks like this:
[CEO, Manager A, Manager B, Intern X, Intern Y, Intern Z]

The Problem: It’s just one giant flat list! You lost all the structural data. If I hand this to the interviewer, they will say: "Wait, is Manager B on floor 2 or floor 3? Are there 6 floors with 1 person each, or 1 floor with 6 people? I can't tell!"

Scenario B: Using TWO lists (With current_floor)
Because we build a fresh current_floor list at the start of every while loop, we group people by their floor before we put them in the main folder.

Floor 1 loop finishes -> We append [CEO] to result.

Floor 2 loop finishes -> We append [Manager A, Manager B] to result.

Floor 3 loop finishes -> We append [Intern X, Intern Y, Intern Z] to result.

Your final answer looks like this:
[  [CEO],  [Manager A, Manager B],  [Intern X, Intern Y, Intern Z]  ]

🏢 The Corporate Analogy
Think of current_floor as a Sign-in Sheet on a clipboard.
Think of result as a Master Filing Cabinet.

You walk out of the elevator onto Floor 2. You grab a blank Sign-in Sheet (current_floor = []).

You make Manager A and Manager B sign it.

You are done with Floor 2. You take that entire Sign-in Sheet and put it into the Master Filing Cabinet (result.append(current_floor)).

You go up to Floor 3, grab a brand new blank Sign-in Sheet, and start again.

By the end of the day, your Master Filing Cabinet doesn't just have a giant pile of loose names. It contains neatly separated pages, one for each floor.
"""
#doubt 2. 
"""
The deque function in Python is strictly designed to take an iterable (like a list, a string, or a tuple) as its starting point. It expects a container of items so it can unpack them and place them into the queue one by one.

What happens if you do deque(root):
The root is just a single TreeNode object (the CEO). If you hand the CEO directly to the deque, Python gets confused. It expects a group of things to loop over, so it tries to "iterate" over the CEO himself. You will immediately get a fatal crash: TypeError: 'TreeNode' object is not iterable.

What happens if you do deque([root]):
By wrapping the root in square brackets [], you are creating a quick, one-item list. You are handing the deque a valid container that happens to hold exactly one passenger (the CEO).
Python says: "Ah, a list! I know how to handle this." It opens the list, pulls the CEO out, and places him perfectly at the front of the queue.

🚌 The Bus Analogy
root = The CEO standing alone on the sidewalk.

[root] = A temporary shuttle bus with the CEO sitting inside.

deque(...) = The queue manager. The manager refuses to talk to pedestrians; they only process people stepping off a shuttle bus.
"""