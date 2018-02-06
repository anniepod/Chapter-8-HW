# Write a function that removes all occurrences of a given letter from a string:

def remove_letter(letter, word):
    new = ""
    for char in word:
        if char == letter:
            new = word[1:char] + word[char:]
            print(new)


remove_letter("a", "apple")

