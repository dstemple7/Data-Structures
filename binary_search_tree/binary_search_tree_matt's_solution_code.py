"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value: # with if, it can do multiple/all unless has return & without recursion at which point it breaks versus with if/elif/else, it will only do one
            if self.right is None: # can be if self.right or if self.right is None or if self.right is not None, then _
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # same thing as mine
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None: # same thing as mine
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # the lowest number is always the furthest to the left
        # recursion requires a base case and a recursive case
        # base case?
        if node is None:
            return
        # if node is none?

        # recursive case?
        self.in_order_print(self.left)

        # build up your call stack to see what happens?

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # iterative so not able to use recursion

        # use a queue
        # start queue with root node

        # while loop
        # checks size of queue
            # pointer variable
            # updates at the beginning of each loop

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # anything you can do with recursion, you can do iteratively if you have a data stack structure
        # use a stack
        # start your stack with the root node

        # while loop that checks stack size
            # pointer        
        
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

    # adding this as getting error on init
    def in_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()