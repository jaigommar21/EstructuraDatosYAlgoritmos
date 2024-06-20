class Node:
    def __init__(self, question=None, left=None, right=None, decision=None):
        self.question = question
        self.left = left
        self.right = right
        self.decision = decision

def build_decision_tree():
    # Leaf nodes
    stay_inside = Node(decision="Stay Inside")
    go_outside = Node(decision="Go Outside")

    # Decision nodes
    is_cold_node = Node(question="Is it cold?", left=stay_inside, right=go_outside)
    is_raining_node = Node(question="Is it raining?", left=stay_inside, right=is_cold_node)

    return is_raining_node

def make_decision(node):
    while node.decision is None:
        answer = input(node.question + " (yes/no): ").strip().lower()
        if answer == "yes":
            node = node.left
        elif answer == "no":
            node = node.right
        else:
            print("Invalid input, please answer 'yes' or 'no'.")
    return node.decision

# Build the decision tree
decision_tree_root = build_decision_tree()

# Make a decision based on user input
activity_decision = make_decision(decision_tree_root)
print(f"Decision: {activity_decision}")