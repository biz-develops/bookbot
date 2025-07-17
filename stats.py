def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowtext = text.lower()
    c_count = {}
    for char in lowtext:
        if char not in c_count:
            c_count[char] = 1
        else:
            c_count[char] += 1
    return c_count

def sort_on(items):
    return items["num"]

def sort_chars(c_dictionary):
    sorted = []
    for c in c_dictionary:
        char_dict = {}
        if c.isalpha():
            sorted.append({"char": c, "num": c_dictionary[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

