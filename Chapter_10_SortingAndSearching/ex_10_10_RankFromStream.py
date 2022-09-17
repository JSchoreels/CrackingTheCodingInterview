class RankSearchTree:

    def __init__(self, data=0, left=None, right=None, rank=0, count=0):
        self.data = data
        self.left: RankSearchTree = left
        self.right: RankSearchTree = right
        self.rank = rank
        self.count = count

    def insert(self, x: int):
        if self.data == x:
            self.rank += 1
            self.count += 1
            if self.right: self.right.rank_all_up()
        elif x < self.data:
            if self.left:
                self.left.insert(x)
            else:
                self.left = RankSearchTree(data=x, rank=self.rank-self.count+1, count=1)
            self.rank += 1
            if self.right: self.right.rank_all_up()
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = RankSearchTree(data=x, rank=self.rank+1, count=1)


    def rank_all_up(self):
        self.rank += 1
        if self.left: self.left.rank_all_up()
        if self.right: self.right.rank_all_up()

    def get_rank(self, x:int):
        if self.data == x:
            return self.rank
        elif x < self.data:
            return self.left.get_rank(x)
        else:
            return self.right.get_rank(x)

    def __repr__(self):
        return f"[{self.left}] ({self.data},r={self.rank},c={self.count}) [{self.right}]"

class StreamRanker:

    def __init__(self):
        self.tree = None


    def track(self, x: int):
        if self.tree is None:
            self.tree = RankSearchTree(data=x, left=None, right=None, rank=0, count=1)
        else:
            self.tree.insert(x)

    def get_rank(self, x:int):
        if not self.tree:
            raise ValueError(f"No item found for x={x}")
        else:
            return self.tree.get_rank(x)


ranker = StreamRanker()
elts = [5, 1, 4, 4, 5, 9, 7, 13, 3]
for elt in elts:
    ranker.track(elt)
    print(ranker.tree)
for elt in elts:
    print(f"Rank of {elt} : {ranker.get_rank(elt)}")