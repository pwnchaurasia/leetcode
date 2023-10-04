class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        full_str = ""
        is_palindrom = True
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric():
                full_str +=i
        j = 0
        k = len(full_str) - 1
        while j < k:
            if full_str[j] == full_str[k]:
                j +=1
                k -=1
            else:
                is_palindrom = False
                break
        return is_palindrom



s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
s = "0P"
sol = Solution()
print(sol.isPalindrome(s=s))