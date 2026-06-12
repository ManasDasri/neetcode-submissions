class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #generating a hashmap for the list

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        sor = sorted(count.items(), key = lambda x: x[1], reverse = "True")

        result = [] 
        for s,t in sor[:k]:
            result.append(s)
        
        return result
        
        


