def count_a(text, letter):
    count = 0
    for c in text:
        if c == letter:
            count += 1
    return(count)
print(count_a("banana", "x"))
