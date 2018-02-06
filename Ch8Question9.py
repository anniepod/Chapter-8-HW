# Write a function that removes all occurrences of a given letter from a string:

def remove_letter(letter, word):
    new = 0
    while new < len(word):
        if word[new] == letter:
            final = word[:letter] + word[letter:]
        new += 1
    return final


remove_letter("a", "apple")

