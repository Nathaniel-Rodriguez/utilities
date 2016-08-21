def chunks_generator(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def chunks_list(l, n):
    """
    returns list instead of a generator
    """

    return [l[i:i + n] for i in xrange(0, len(l), n)]

if __name__ == '__main__':
    pass