"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def recursive_help(word, count=0):
    if len(word) <= 1:
        return count
    if word[:2] == "th":
        count += 1

    return recursive_help(word[1:], count)


def count_th(word):
    return recursive_help(word, count=0)

