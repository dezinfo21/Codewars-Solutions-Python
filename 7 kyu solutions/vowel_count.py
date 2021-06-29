def get_count(input_str):
    return sum(1 for v in input_str if v in ['a', 'e', 'i', 'o', 'u'])
