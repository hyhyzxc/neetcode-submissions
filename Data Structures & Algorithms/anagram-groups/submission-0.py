from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        currIndex = 0
        hashMap = {}

        for word in strs:
            countArr = [0] * 26
            for char in word:
                countArr[ord(char) - 97] += 1
            wordKey = tuple(countArr)
            if wordKey in hashMap:
                res[hashMap[wordKey]].append(word)
            else:
                hashMap[wordKey] = currIndex
                res.append([word])
                currIndex += 1
        
        return res

        
        
            

        