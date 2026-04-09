from queue import PriorityQueue

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 存储三元组 (num1[i], nums2[i], i)
        # i 记录 nums2 元素的索引位置，用于生成下一个节点
        pq = PriorityQueue()
        
        # 按照 23 题的逻辑初始化优先级队列
        for i in range(len(nums1)):
            pq.put((nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        res = []
        # 执行合并多个有序链表的逻辑
        while not pq.empty() and k > 0:
            _, num1, num2, idx = pq.get()
            k -= 1
            # 链表中的下一个节点加入优先级队列
            next_index = idx + 1
            if next_index < len(nums2):
                pq.put((num1 + nums2[next_index], num1, nums2[next_index], next_index))

            # 按照数对的元素和升序排序
            pair = [num1, num2]
            res.append(pair)

        return res
        