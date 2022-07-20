

import random


class Words():
    def __init__(self) -> None:
        fp = open('words.txt', 'r')
        words = fp.read()
        self.words = words.split('\n')
        fp.close()
    
    def get(self, n: int = 20):
        ret = []
        for _ in range(n):
            ret.append(random.choice(self.words))
        
        return " ".join(ret)
    
    def get_by_letter(self, letter: str, n: int = 20):
        ret = []
        for _ in range(n):
            m = random.random()
            if m > 0.75:
                if m > 0.95:
                    word = self._get_word_by_letter(letter, 3)
                else:
                    word = self._get_word_by_letter(letter, 2)
            else:
                word = self._get_word_by_letter(letter, 1)
            ret.append(word)
        return " ".join(ret)
    
    def _get_word_by_letter(self, letter: str, count: int):
        for word in self.words:
            c = 0
            for i in word:
                if i == letter:
                    c+=1
            if c >= count:
                return word