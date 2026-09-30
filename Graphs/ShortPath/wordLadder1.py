# https://leetcode.com/problems/word-ladder/

from typing import List
from queue import Queue
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set()
        st.update(wordList)
        q = Queue()
        q.put((beginWord, 1))

        length = len(beginWord)

        if endWord not in st:
            return 0

        st.discard(beginWord)

        while not q.empty():
            word, step = q.get()
            for i in range(length):
                for ch in string.ascii_lowercase:
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in st:
                        if newWord == endWord:
                            return step + 1
                        st.remove(newWord)
                        q.put((newWord, step + 1))

        return 0