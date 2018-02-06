#Write a function that removes the first occurrence of a string from another string:

def remove(phrase, word):
    new = word.replace(phrase, "")
    return new


print(remove("yes", "yesooo"))
