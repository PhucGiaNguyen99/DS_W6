import sys


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left if left != -1 else None
        self.right = right if right != -1 else None


class TreeOrders:
    def __init__(self):
        self.nodes = []
        self.root = None
        self.result_inorder = []
        self.result_preorder = []
        self.result_postorder = []

    def read(self):
        n = int(sys.stdin.readline())
        for i in range(n):
            key, left, right = map(int, sys.stdin.readline().split())
            node = Node(key, left, right)
            self.nodes.append(node)
        self.root = self.nodes[0]

    def inorder(self, node):
        if not node:
            return

        if node.left:
            self.inorder(self.nodes[node.left])

        self.result_inorder.append(node.key)

        if node.right:
            self.inorder(self.nodes[node.right])

    def preorder(self, node):
        if not node:
            return

        self.result_preorder.append(node.key)
        if node.left:
            self.preorder(self.nodes[node.left])
        if node.right:
            self.preorder(self.nodes[node.right])

    def postorder(self, node):
        if not node:
            return

        if node.left:
            self.postorder(self.nodes[node.left])

        if node.right:
            self.postorder(self.nodes[node.right])
        self.result_postorder.append(node.key)

    def run_traversals(self):
        self.inorder(self.root)
        self.preorder(self.root)
        self.postorder(self.root)