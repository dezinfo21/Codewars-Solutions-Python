def greet_developers(lst):
    for x in lst:
        x['greeting']='Hi {}, what do you like the most about {}?'.format(x['firstName'], x['language'])
    return lst
