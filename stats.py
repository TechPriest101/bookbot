def get_words_count(text):
    words = text.split()
    return len(words)


def get_characters_count(text):
    characters_count = {}
    for i in text:
        c = i.lower()
        if c in characters_count:
            characters_count[c] += 1
        else:
            characters_count[c] = 1
    return characters_count


def sorted_list_of_dictionaries(dictionary):
    sorted_list = []
    for i in dictionary:
        sorted_list.append({"char": i, "num": dictionary[i]})

    def sort_on(items):
        return items["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
