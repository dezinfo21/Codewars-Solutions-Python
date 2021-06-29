def printer_error(s):
    a = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    error_num = sum(1 for _ in s if _.lower() in a)
    return(str(error_num) + '/' + str(len(s)))
