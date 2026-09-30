# https://leetcode.com/problems/word-ladder-ii/

from queue import Queue
from typing import List
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        st = set(wordList)

        if endWord not in st:
            return []

        q = Queue()
        q.put([beginWord])

        if beginWord in st:
            st.remove(beginWord)

        ans = []
        found = False

        while not q.empty():
            level_size = q.qsize()
            used = set()
            
            for _ in range(level_size):
                path = q.get()
                word = path[-1]

                if word == endWord:
                    ans.append(path)
                    found = True
                    continue

                for i in range(len(word)):

                    for ch in string.ascii_lowercase:

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i+1:]

                        if new_word in st:
                            new_path = path + [new_word]
                            q.put(new_path)
                            used.add(new_word)

            for word in used:
                st.remove(word)

            if found:
                break

        return ans