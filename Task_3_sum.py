import uuid
from draw_tree import draw_tree


class Node:
    def __init__(self, key, color="green"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_sum(node):
    if node is None:
        return 0
    
    return node.val + find_sum(node.left) + find_sum(node.right)


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 11)
    root = insert(root, 12)
    root = insert(root, 8)
    root = insert(root, 10)
    root = insert(root, 1)
    
    #draw_tree(root)
    
    sum_value = find_sum(root)
    print(f"\nSum value: {sum_value}\n")
   