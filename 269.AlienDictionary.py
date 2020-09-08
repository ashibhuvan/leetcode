
from typing import List

#test case
word = ["wrt","wrf","er","ett","rftt"]
class Solution:
    def alienOrder(self,words:List[str]) -> str:

        dict = {}
        if len(words) == 1:
            return words[0]
        for idx,val in enumerate(words[0]):
            dict.update({val:idx})

        words = words[1:]
        print(dict)
        print(words)
bob = Solution()
print(bob.alienOrder(word))




