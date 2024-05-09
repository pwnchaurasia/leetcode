class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False   # flagging every word false and last word will be flagged true to differentiate

    def addWord(self, word):
        cur = self
        for c in word:       # the first letter of every word will be the direct children of root node containing a-z, A-Z, 0-9, etc as the first word
            if c not in cur.children:  # when the word not in roots direct children, then create a direct node for it
                cur.children[c] = TrieNode()
            cur = cur.children[c]      # if the first word is present as a child of root node, then append the word to that children
        cur.endOfWord = True # when for loop ends means we are on the last word, we are flagging the last as true to differ between last, first and mid words


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:  # Time: O(n*n) and Space: O(n*n)
        root = TrieNode()
        for w in words:            # adding the words from word list to the prefix tree
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # using set, so we will be able to eliminate duplication

        def dfs(r, c, node, word):
		    # i,j should not be less than 0, i and j should not be equal to the length as i,j starts from 0 not from 1,
			# it should not be already visited, and if the word is not the direct children of root
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))   # if all the above conditions fail then mark the word visited
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:  # if node is flagged True means we have reached the end of tree and matched perfectly the words from word list
                res.add(word)   # then append the matched word in the res so we can return it

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
			# after taking the word[r,c] as the first word and visiting every possible variation, we unmarked it for further use in other variations
            visit.remove((r, c))

        for r in range(ROWS):        # visiting every word from the board
            for c in range(COLS):
                dfs(r, c, root, "")  # passing the i, j index, prefix tree, and matched word between word list and board words

        return list(res)