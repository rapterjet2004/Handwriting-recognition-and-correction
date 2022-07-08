import numpy as np

class WordSearcher:

    def __init__(self) -> None:
        self.array = np.loadtxt("words_alpha.txt", str)

    
    def binarySearchWords(self, query: str) -> bool:
        """
        Searches through the English dictionary, return True is word exists, False otherwise
        """
        if query.isalpha():
            left = 0 
            right = len(self.array)

            while left < right:
                m = int((left + right) / 2)      
                if self.array[m] == query:
                    return True
                elif self.isGreater(self.array[m], query):
                    right = m
                else:
                    left = m + 1

        return False

    
    def isGreater(self, current: str, query: str) -> bool:
        """
        Returns True if current string is greater alphabetically than query, False otherwise
        """    
        for char in range(len(min(current, query))):
            if current[char] != query[char]:
                if ord(current[char]) > ord(query[char]):
                    return True
                else:
                    return False
        
        # if the loop terminated w/o returning anything, then both query and current are equal until the 
        # end of the smaller word
        #   
        # for example: current = "an" and query = "and", logically now the longer word is alphabetically 
        # greater
        if min(current, query) == current:
            return False
        else:
            return True



