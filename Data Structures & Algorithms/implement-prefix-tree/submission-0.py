class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = []

class PrefixTree:
    def __init__(self):
        self.root = Node("0")

    def insert(self, word: str) -> None:
        dex = 0
        curr = self.root
        while dex != len(word):
            letter = word[dex]
            found = False
            for i in range(len(curr.next)):
                nxt_ltr = curr.next[i]
                if nxt_ltr.val == letter and len(nxt_ltr.next) > 0 and dex < len(word) - 1:
                    curr = curr.next[i]
                    found = True
                    break
            if not found:
                curr.next.append(Node(letter))
                curr = curr.next[-1]
            
            dex += 1

    def search(self, word: str) -> bool:
        dex = 0
        word_len = len(word) - 1
        curr = self.root
        while dex != len(word):
            letter = word[dex]
            found = False
            for i in range(len(curr.next)):
                nxt_ltr = curr.next[i]
                len_nxt_ltr = len(nxt_ltr.next)

                if nxt_ltr.val == letter:
                    if dex == word_len and len_nxt_ltr == 0:
                        return True
                    if dex != word_len and len_nxt_ltr > 0:
                        curr = curr.next[i]
                        dex += 1
                        found = True
                        break   
            if not found:
                return False

    def startsWith(self, prefix: str) -> bool:
        dex = 0
        pref_len = len(prefix) - 1
        curr = self.root
        while dex != len(prefix):
            letter = prefix[dex]
            found = False
            for i in range(len(curr.next)):
                nxt_ltr = curr.next[i]
                len_nxt_ltr = len(nxt_ltr.next)

                if nxt_ltr.val == letter:
                    if dex == pref_len: return True
                    if dex != pref_len and len_nxt_ltr > 0:
                        curr = curr.next[i]
                        dex += 1
                        found = True
                        break
            if not found:
                return False
        
        