class BSTNode:
    def __init__(self, key: int, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, key, value=None):
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            self.root = BSTNode(key, value) # type: ignore
            self._size += 1
            return

        if type(key) is not type(self.root.key):
            raise TypeError

        current = self.root
        while True:
            if key == current.key:
                current.value = value
                return
                
            elif key < current.key: # type: ignore
                if current.left is None:
                    current.left = BSTNode(key, value) # type: ignore
                    self._size += 1
                    return
                current = current.left
                
            else:
                if current.right is None:
                    current.right = BSTNode(key, value) # type: ignore
                    self._size += 1
                    return
                current = current.right



    def contains(self, key):
            if not isinstance(key, (int, str)):
                raise TypeError
    
            if self.root is None:
                return False
    
            current = self.root
            while True:
                if key == current.key:
                    return True
                    
                elif key < current.key: # type: ignore
                    if current.left is None:
                        return False
                    current = current.left
                    
                else:
                    if current.right is None:
                        return False
                    current = current.right
    
    def get(self, key):
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            return False

        current = self.root
        while True:
            if key == current.key:
                return current.value
                
            elif key < current.key: # type: ignore
                if current.left is None:
                    raise KeyError
                current = current.left
                
            else:
                if current.right is None:
                    raise KeyError
                current = current.right


    def delete(self, key):
        if not isinstance(key, (int, str)):
            raise TypeError

        if self.root is None:
            return False

        parent = None
        current = self.root

        while True:
            if key == current.key:
                # Case 1: Leaf Node (0 children)
                if current.left is None and current.right is None:
                    if current == self.root:
                        self.root = None
                    elif parent.left == current: # type: ignore
                        parent.left = None # type: ignore
                    else:
                        parent.right = None # type: ignore

                # Case 2a: Only Left Child
                elif current.left is not None and current.right is None:
                    if current == self.root:
                        self.root = current.left
                    elif parent.left == current: # type: ignore
                        parent.left = current.left # type: ignore
                    else:
                        parent.right = current.left # type: ignore

                # Case 2b: Only Right Child
                elif current.left is None and current.right is not None:
                    if current == self.root:
                        self.root = current.right
                    elif parent.left == current: # type: ignore
                        parent.left = current.right # type: ignore
                    else:
                        parent.right = current.right # type: ignore

                # Case 3: 2 Children
                else:
                    succ_parent = current
                    inorder_successor = current.right
                    
                    # Walk left to find the smallest node in right subtree
                    while inorder_successor.left is not None: # type: ignore
                        succ_parent = inorder_successor
                        inorder_successor = inorder_successor.left # type: ignore

                    # Copy BOTH key and value over
                    current.key = inorder_successor.key # type: ignore
                    current.value = inorder_successor.value # type: ignore

                    # Unhook the successor node from its parent
                    if succ_parent.left == inorder_successor: # type: ignore
                        succ_parent.left = inorder_successor.right # type: ignore
                    else:
                        succ_parent.right = inorder_successor.right # type: ignore

                self._size -= 1
                return True

            elif key < current.key: # type: ignore
                if current.left is None:
                    return False
                parent = current
                current = current.left

            else:
                if current.right is None:
                    return False
                parent = current
                current = current.right

    

    def inorder(self):
        result = []
        stack = []
        current = self.root
        
        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.key)
            
            current = current.right
            
        return result
                

        

    def preorder(self):
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.key)

            # Push right first so left is popped and processed first
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

        return result



    def postorder(self):
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.key)

            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)

        return result[::-1]

    
    
    def level_order(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.key)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result



    def height(self):
        if self.root is None:
            return 0

        queue = [self.root]
        height = 0

        while len(queue) > 0:
            level_size = len(queue)
            height += 1

            # Process all nodes currently in this level
            for useless_i in range(level_size):
                current = queue.pop(0)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return height
        

    def min_key(self):
        if self._size == 0:
            raise ValueError

        current = self.root
        while current.left is not None: # type: ignore
            current = current.left # type: ignore

        return current.key # type: ignore

    def max_key(self):
        if self._size == 0:
            raise ValueError

        current = self.root
        while current.right is not None: # type: ignore
            current = current.right # type: ignore

        return current.key # type: ignore


    def count_leaves(self):
        if self.root is None:
            return 0

        leaf_num = 0
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.left is None and current.right is None:
                leaf_num += 1

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return leaf_num

    def range_query(self, low, high):
        if type(low) is not int or type(high) is not int:
            raise TypeError

        results = []
        stack = []
        current = self.root

        while current or stack:
            # Drill down left only if current key is strictly greater than low
            while current is not None:
                stack.append(current)
                if current.key > low:
                    current = current.left
                else:
                    current = None  # Prune left subtree

            current = stack.pop()

            # Check if current key falls within the inclusive range
            if low <= current.key <= high:
                results.append(current.key)

            # Explore right subtree only if current key is strictly less than high
            if current.key < high:
                current = current.right
            else:
                current = None  # Prune right subtree

        return results

    def is_valid_bst(self):
        if self.root is None:
            return True

        stack = [(self.root, None, None)]
        while stack:
            node, min_bound, max_bound = stack.pop()

            if min_bound is not None and node.key <= min_bound:
                return False
            if max_bound is not None and node.key >= max_bound:
                return False

            if node.right:
                stack.append((node.right, node.key, max_bound)) # type: ignore

            if node.left:
                stack.append((node.left, min_bound, node.key)) # type: ignore

        return True

        return True

    def is_empty(self):
        return self.root is None
    
    def __len__(self):
        return self._size