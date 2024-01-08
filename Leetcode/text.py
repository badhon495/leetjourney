"leetcode 589"

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root):
    if not root:
        return []
    res = []
    res.append(root.val)
    for child in root.children:
        res.extend(preorder(child))
    return res

def preorder2(root):
    if not root:
        return []
    res = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        for child in node.children[::-1]:
            stack.append(child)
    return res

def preorder3(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.children[0]
        node = stack.pop()
        node = node.children[1]
    return res

def preorder4(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.children[0]
        node = stack.pop()
        node = node.children[1]
    return res

def preorder5(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.children[0]
        node = stack.pop()
        node = node.children[1]
    return res

def preorder6(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.children[0]
        node = stack.pop()
        node = node.children[1]
    return res


