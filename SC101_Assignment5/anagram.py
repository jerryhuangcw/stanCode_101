"""
File: anagram.py
Name: Jerry Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
# Global var
dictionary_lst = []  # stores all words in dictionary.txt
anagram_lst = []  # stores all anagrams found in dictionary

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    global anagram_lst
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        search = input('Find anagrams for: ')
        if search == EXIT:
            break
        else:
            search = search.lower()
            print('Searching...')
            find_anagrams(search)
        print(f'{len(anagram_lst)} anagrams:', anagram_lst)
        anagram_lst = []


def find_anagrams(s):
    num_lst = []
    for i in range(len(s)):
        num_lst.append(i)  # Give every alphabet an code
    helper(s, num_lst, [])


def helper(s, num_lst, current_lst):
    global anagram_lst
    if len(current_lst) == len(s):
        anagram = ''
        for j in range(len(s)):
            ele = current_lst[j]
            anagram += s[ele]  # convert the codes back to alphabets and string them
            if has_prefix(anagram) is True:
                if anagram not in anagram_lst and len(anagram) == len(s) and anagram in dictionary_lst:
                    print('Found:', anagram)
                    print('Searching...')
                    anagram_lst.append(anagram)
        else:
            pass
    else:
        for num in num_lst:
            if num not in current_lst:
                current_lst.append(num)
                helper(s, num_lst, current_lst)
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: first two letters of the anagram
    :return: bool
    """
    if sub_s in dictionary_lst:
        return True


def read_dictionary():
    global dictionary_lst
    with open(FILE, 'r') as f:
        for line in f:
            dictionary_lst.append(line.strip())


if __name__ == '__main__':
    main()
