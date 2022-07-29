# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return ("Node({})".format(self.value))

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    @property
    def printInorder(self):
        if self.isEmpty():
            return None
        else:
            self._inorderHelper(self.root)

    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left)
            print(node.value, end=' : ')
            self._inorderHelper(node.right)

    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def _mirrorHelper(self, node):

        ans = node
        l = [node]
        while len(l) != 0:
            cur = l[0]
            del l[0]

            if cur.left is not None:
                prev1 = cur.left
                prev2 = cur.right
                cur.left = prev2
                cur.right = prev1

            elif cur.right is not None:
                prev1 = cur.left
                prev2 = cur.right
                cur.left = prev2
                cur.right = prev1

            if cur.left is not None:
                l.append(cur.left)

            if cur.right is not None:
                l.append(cur.right)
        return ans


    @property
    def getMin(self):
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur


    @property
    def getMax(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur

    def __contains__(self, value):
        cur = self.root
        while cur is not None:
            if value == cur.value:
                return True
            elif value > cur.value:
                cur = cur.right
            else:
                cur = cur.left
        return False

    def getHeight(self, node):
        hmax = self._getHeightHelper(self.root)

        h = 0
        cur = self.root
        while node.value != cur.value:
            h += 1
            if node.value > cur.value:
                cur = cur.right
            else:
                cur = cur.left
        return hmax - h

    def _getHeightHelper(self, node):
        if node is None:
            return -1
        else:
            lh = self._getHeightHelper(node.left)
            rh = self._getHeightHelper(node.right)

            if lh > rh:
                return lh + 1
            else:
                return rh + 1

