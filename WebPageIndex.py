
class AVLnode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = None


class AVLtree:

    def __init__(self, file):
        f = open(file, "r")
        contents = f.read().lower()
        f.close()
        punctuation = '''!()[]{};:'",<>./\?@#$%^&*_~'''
        no_punct = " "
        for char in contents:
            if char not in punctuation:
                no_punct += char
            else:
                no_punct += " "
        words = no_punct.split()
        no_duplicates = list(dict.fromkeys(words))
        key_vals = []
        for word in no_duplicates:
            pos = []
            for i in range(len(words)):
                if words[i] == word:
                    pos.append(i)
            key_vals.append([word,pos])

        self.root = AVLnode(key_vals[0][0], key_vals[0][1])
        for i in range(1,len(key_vals)-1):
            self.put(key_vals[i][0], key_vals[i][1])

    def getCounts(self, s):
        a = self.search(s, self.root)
        if a != None:
            return len(a.value)
        return None


    def get(self, data):

        a = self.search(data, self.root)
        if a != False:
            return a.value
        return None

    def search(self, data, cur_node):
        if cur_node == None:
            return False

        elif data == cur_node.key:
            return cur_node

        if data < cur_node.key:
            return self.search(data, cur_node.left)
        else:
            return self.search(data, cur_node.right)

    def put(self, data, value=None):
        data = AVLnode(data, value)
        y = None
        x = self.root

        while x != None:
            y = x
            if data.key < x.key:
                x = x.left
            else:
                x = x.right

        data.parent = y

        if y == None:
            self.root = data

        elif data.key < y.key:
            y.left = data
        else:
            y.right = data

        self.setHeight(data, data.key)

    def setHeight(self, node, newInsert=None):
        newInsert = newInsert
        node.height = self._setHeight(node)

        if newInsert != None:
            self.unbalanceDetector(node, newInsert)

        if node.parent != None:
            self.setHeight(node.parent, newInsert)

    def _setHeight(self, node):

        if node == None:
            return 0
        left = self._setHeight(node.left)
        right = self._setHeight(node.right)
        return max(left, right) + 1

    def __setHeight(self, node):

        if node != None:
            node.height = self._setHeight(node)
            self.__setHeight(node.left)
            self.__setHeight(node.right)

    def unbalanceDetector(self, node, newInsert):

        root = node
        if root.left != None:
            leftH = root.left.height

        else:
            leftH = 0

        if root.right != None:
            rightH = root.right.height
        else:
            rightH = 0

        bHeight = leftH - rightH

        if bHeight < -1 or bHeight > 1:
            self.directionDetector(node, bHeight, newInsert)

    def directionDetector(self, node, bfctor, newInsert):

        if bfctor > 1 and newInsert < node.left.key:
            self.leftRoation(node)

        elif bfctor < -1 and newInsert > node.right.key:
            self.rightRoation(node)

        elif bfctor > 1 and newInsert > node.left.key:
            self.rightRoation(node.left)
            self.leftRoation(node)

        elif bfctor < -1 and newInsert < node.right.key:
            self.leftRoation(node.right)
            self.rightRoation(node)

    def leftRoation(self, node):

        root = node
        pivot = node.left  # find the pivot in left side

        root.left = pivot.right  # move the right child of pivot to root
        # FIX2: add parent reset
        if pivot.right != None:
            pivot.right.parent = root
        pivot.right = root  # then pivot has right child root

        # reset their parent
        pivot.parent = root.parent
        root.parent = pivot

        # if the pivot has parent
        if pivot.parent != None:

            # depends if pivot is in his parent left or right
            # according to the postion, insert pivot as child to his parent
            # FIX1: need to check if pivot.parent.left exists or not
            if pivot.parent.left != None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot

            # reset the height for parent above
            self.setHeight(pivot.parent)
        else:
            self.root = pivot

        # reset the height for pivot
        self.__setHeight(pivot)

    def rightRoation(self, node):

        root = node
        pivot = node.right

        root.right = pivot.left
        # FIX2: add parent reset
        if pivot.left != None:
            pivot.left.parent = root
        pivot.left = root

        pivot.parent = root.parent
        root.parent = pivot

        if pivot.parent != None:
            # FIXED: need to check if pivot.parent.left exists or not
            if pivot.parent.left != None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot

            self.setHeight(pivot.parent)
        else:
            self.root = pivot
        self.__setHeight(pivot)

    # Printing the tree
    def printTree(self):
        print("new tree:")
        self.__printTree(self.root)

    def __printTree(self, node, level=0):
        if node is None:
            return
        if node.value != None:
            self.__printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', str(node.key) + "," + str(node.value) + "," + str(node.height))
            self.__printTree(node.right, level + 1)


