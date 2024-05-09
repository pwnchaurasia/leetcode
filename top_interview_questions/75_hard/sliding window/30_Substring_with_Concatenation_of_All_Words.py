class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0: return []

        count = {}
        word_len = len(words[0])
        res = []
        words_len = len(words) * word_len
        for word in words:
            count[word] = count.get(word, 0) + 1

        for left in range(len(s) - words_len + 1):
            words_seen = {}

            for right in range(len(words)):
                word_index = left + right * word_len
                temp_word = s[word_index: word_index+word_len]

                if temp_word not in count:
                    break
                words_seen[temp_word] = words_seen.get(temp_word, 0) + 1
                if words_seen[temp_word] > count[temp_word]:
                    break

            if words_seen == count:
                res.append(left)
        return res














