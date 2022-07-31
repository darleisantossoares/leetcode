class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find_root_parent(node):

            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res


        def union(node_1, node_2):

            parent1, parent2 = find_root_parent(node_1), find_root_parent(node_2)

            if parent1 == parent2:
                return 0

            if rank[parent2] > rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)


        return res

        # O(E * log(V))
