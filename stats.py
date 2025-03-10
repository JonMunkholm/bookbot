def get_num_words(data):
    str = data.split()
    return len(str)

def char_count(data):

    res = {}
    for char in data.lower():
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1
    return res

def sort_char_count(arg):
    res = dict(sorted(arg.items(), key=lambda item: item[1], reverse=True))
    return {x:y for x, y in res.items() if x.isalpha()}
