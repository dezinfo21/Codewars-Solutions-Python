def get_first_python(users):
    return '{}, {}'.format(list(filter(lambda x: x['language']=='Python', users))[0]['first_name'], list(filter(lambda x: x['language']=='Python', users))[0]['country']) if any(x['language']=='Python' for x in users) else 'There will be no Python developers'
