class WUF:
    """This class implements the Weighted Union Find (WUF) data structure for contact tracing """

    Pair = tuple[str, int]
    """A data type used to combine the root and size information into a single location."""

    tree = {}
    """The tree is used to store the data."""

    def __init__(self, iTree: dict[str, Pair] = None):
        """initializes the WUF.

        A fairly standard __init__ function to initliaze the data necessary for the WUF.
        If a tree is not provided, an empty tree is created.

        :param self: self
        :param iTree: the tree structure to construct the WUF from
        :type iTree: dict[str, (str, int)]
        """
        if not iTree:
            iTree = {}

        self.tree = iTree

    def getRoot(self, uid: str) -> str:
        """returns the root of the union the id is in

        This function traverses the tree in order to find the root of the union that ID is a part of.

        :param self: self
        :param uid: the Student ID to retrieve the union for
        :type uid: str
        :returns: the root student ID in the union
        :rtype: str
        """

        root = uid
        while root != self.tree[root][0]:
            root = self.tree[root][0]

        return root

    def union(self, p: str, q: str) -> None:
        """unions two items in the tree

        Unions data in the tree using the WUF alorithm.
        If the size of q's root union is greater than the size of p's root union, then add p to q.
        Otherwise, q will be added to p.

        :param self: Self
        :param p: the first item to union
        :param q: the second item to union
        :type p: str
        :type q: str
        """

        pRoot = self.getRoot(p)
        qRoot = self.getRoot(q)

        if pRoot == qRoot:
            return

        if self.tree[qRoot][1] > self.tree[pRoot][1]:
            self.tree[pRoot][0] = qRoot
            self.tree[qRoot][1] += self.tree[pRoot][1]
        else:
            self.tree[qRoot][0] = pRoot
            self.tree[pRoot][1] += self.tree[qRoot][1]
