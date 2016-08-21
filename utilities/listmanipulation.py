def chunk_generator(l, n):
    """
    Attempts to divide list into chunks of size n
    Returns a generators that yields successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def chunk_list(l, n):
    """
    Attempts to divide list into chunks of size n
    """

    return [l[i:i + n] for i in xrange(0, len(l), n)]

def split_list(a, n):
    """
    Splits list into n parts
    """

    k, m = len(a) / n, len(a) % n
    return [a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n)]

if __name__ == '__main__':
    pass