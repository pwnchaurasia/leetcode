
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        create_hash_table = {}
        for i in magazine:
            if i in create_hash_table:
                create_hash_table[i] +=1
            else:
                create_hash_table[i] = 1
        
        ransomeNote_dict = {}
        for i in  ransomNote:
            if i in ransomeNote_dict:
                ransomeNote_dict[i] += 1
            else:
                ransomeNote_dict[i] = 1

        for i in ransomeNote_dict:
            if i not in create_hash_table or create_hash_table[i] < ransomeNote_dict[i]:
                return False
        return True





sol = Solution()
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))