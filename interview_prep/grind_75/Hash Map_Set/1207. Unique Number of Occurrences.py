from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashed = {}
        for i in arr:
            hashed[i] = hashed.get(i, 0) + 1

        # value_set = set()
        # res = True
        # for i in hashed:
        #     if hashed[i] not in value_set:
        #         value_set.add(hashed[i])
        #     else:
        #         res = False
        #         break
        # return res
        # above works well
        # but we can do better
        return len(set(hashed.values())) == len(hashed.values())

if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    # arr = [1, 2]
    print(sol.uniqueOccurrences(arr=arr))
