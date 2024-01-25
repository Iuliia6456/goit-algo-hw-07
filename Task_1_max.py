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


def find_max_value(node):
    if node is None:
        return None
    
    while node.right is not None:
        node = node.right

    return node.val


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
    
    draw_tree(root)
    
    max_value = find_max_value(root)
    print(f"\nMaximum value: {max_value}\n")