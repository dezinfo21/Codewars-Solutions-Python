def is_ruby_coming(lst): 
    return any(x['language']=='Ruby' for x in lst)
