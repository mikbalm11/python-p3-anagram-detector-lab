class Anagram:
    '''A class to find anagrams of a given word.'''

    def __init__(self, word):
        '''Initialize with a word.'''
        self.word = word

    def match(self, words):
        '''Find all anagrams of the given word in the list.'''
        matchlist = []
        for word in words:
            if sorted(self.word.lower()) == sorted(word.lower()):
                matchlist.append(word)
        return matchlist
