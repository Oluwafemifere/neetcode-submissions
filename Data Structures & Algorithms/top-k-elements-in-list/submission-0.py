class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        # buckets = [[], [3], [2], [1], [], [], []]

        result = []
        for freq in range(len(buckets) - 1, 0, -1):   # highest count first
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result