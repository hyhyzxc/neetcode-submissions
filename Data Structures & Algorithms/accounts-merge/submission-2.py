from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
            nameMap = {}
            for i in range(len(accounts)):
                nameMap[i] = accounts[i][0]

            rootMap = {}
            rankMap = defaultdict(int)

            for i in range(len(accounts)):
                rootMap[i] = i
                rankMap[i] += 1
            
            def find(i):
                while rootMap[i] != i:
                    rootMap[i] = rootMap[rootMap[i]]
                    i = rootMap[i]
                return i
            
            def union(nameIndex, email):

                if email not in rootMap:
                    rootMap[email] = nameIndex
                    rankMap[nameIndex] += 1
                else:
                    rootName, rootEmail = find(nameIndex), find(email)
                    rankName, rankEmail = rankMap[rootName], rankMap[rootEmail]
                    if rankName > rankEmail:
                        rankMap[rootName] += rankMap[rootEmail]
                        rootMap[rootEmail] = rootName
                    else:
                        rankMap[rootEmail] += rankMap[rootName]
                        rootMap[rootName] = rootEmail
            
            for i, details in enumerate(accounts):
                emailList = details[1:]
                for email in emailList:
                    union(i, email)
                for i in range(len(emailList)):
                    for j in range(i + 1, len(emailList)):
                        union(emailList[i], emailList[j])

            res = defaultdict(list)
            for i in rootMap:
                rootMap[i] = find(i)
                if type(i) is int:
                    continue
                else:
                    res[rootMap[i]].append(i)
            arrayRes = []
            for i in res:
                currAccounts = [nameMap[i]]
                currAccounts += sorted(res[i])
                arrayRes.append(currAccounts)
            return arrayRes

                    
            

            



