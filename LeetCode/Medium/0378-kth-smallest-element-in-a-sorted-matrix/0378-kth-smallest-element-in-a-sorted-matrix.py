from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 存储二元组 (matrix[i][j], i, j)
        # i, j 记录当前元素的索引位置，用于生成下一个节点
        pq = PriorityQueue()

        # 初始化优先级队列，把每一行的第一个元素装进去
        for i in range(len(matrix)):
            pq.put((matrix[i][0], i, 0))

        res = -1
        # 执行合并多个有序链表的逻辑，找到第 k 小的元素
        while not pq.empty() and k > 0:
            cur = pq.get()
            # 按照元素大小升序排序
            res = cur[0]
            k -= 1
            # 链表中的下一个节点加入优先级队列
            i, j = cur[1], cur[2]
            if j + 1 < len(matrix[i]):
                pq.put((matrix[i][j + 1], i, j + 1))
        return res