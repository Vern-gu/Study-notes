class Node:
    """树的节点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree:
    """二叉树"""
    def __init__(self):
        self.root = None
    def add(self,item):
        """树的添加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]  # 使用队列的模式
        while queue:  # 只要队列不为空就一直可以循环
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        """树的广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            elif cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self,node):  # 深度优先遍历，分为先序、中序、后序
        """前序遍历"""        # 根-左-右
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def inorder(self,node):  # 左-根-右
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)
    def postorder(self,node):  # 左-右-根
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)


tree = Tree()
