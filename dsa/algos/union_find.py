class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False 
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.rank[p1] = p2
        else:
            self.par[p1] = p2 
            self.rank[p2] += 1
        return True

if __name__ == '__main__':
    u = UnionFind(10)
    print(u.find(4))
    print(u.union(2,3))
    print(u.union(4, 1))
    print('*' * 10)
    print('RANK')
    print(u.rank)
    print('*' * 10)
    print('PARENTS')
    print(u.par)