var = "abcabcdabcef"

def longest_substring(string):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(string)):
        while string[right] in seen:
            seen.remove(string[left])
            left += 1
        seen.add(string[right])
        max_length = max(max_len, right - left + 1)