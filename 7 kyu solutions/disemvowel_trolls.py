def disemvowel(string_):
    return ''.join(x for x in string_ if x.lower() not in ['a', 'e', 'i', 'o', 'u'])
