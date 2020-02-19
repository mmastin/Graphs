# directed or undirected?
# cyclic, acyclic?
# dense, sparse?

# undirected, cyclic, sparse

# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# 1. Translate the problem into graph terminology
# 2. Build your graph
# 3. Traverse your graph

from util import Stack, Queue

f = open('/Users/mattmastin/Desktop/Graphs/projects/graph/words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set([w.lower() for w in words])

def get_neighbors(w):
    """
    return all words in word_set that have 1 and only 1 letter different
    """
    # for each letter in the word
    neighbors = []
    alphabet = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_list = list(w)
    for i in range(len(letter_list)):
        # for each letter in the alphabet
        # O(m) where m is the number of letters in the alphabet
        for letter in alphabet:
            # replace the word letter with that alphabet
            temp_word = list(letter_list)
            temp_word[i] = letter
            new_word = ''.join(temp_word)
            # letter and check if resulting word in word_set
            if new_word in word_set and new_word in w:
            # if so, add to neighbor list
                neighbors.append(new_word)
    return neighbors

# get_neighbors('cat')

def find_ladders(begin_word, end_word):
    """
    find a word transformation between begin and end word.
    Use BFS
    """
    q = Queue()
    # enqueue path to starting word
    q.enqueue( [begin_word] )
    visited = set()
    # while queue is not empty
    while q.size() > 0:
        # dequeue path
        path = q.dequeue()
        # grab last word from path
        w = path[-1]
        # check if it's target word, if sor eturn path
        if w == end_word:
            return path
        # check if it's been visited, if not...
        if w not in visited:
            # mark it as visited
            visited.add(w)
            # enqueue a path to match neighbor
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None

print(find_ladders('sail', 'boat'))