def maskify(cc):
    return cc if len(cc) <= 4 else '#'*(len(cc)-4)+cc[len(cc)-4:]
