import numpy as np
from scipy.stats import bayes_mvs

def bayes_mvs_wrapper(sequence, alpha):

    if max(sequence) == min(sequence):
        return (np.mean(sequence), (np.mean(sequence), np.mean(sequence))), (0, (0,0)), (0, (0,0))
    else:

        return bayes_mvs(sequence, alpha)

def log_linspace(start, stop, number):
    """
    Like linspace, only for evenly spaced log-values.
    """
    
    lstart = np.log(start)
    lstop = np.log(stop)
    ldata = np.linspace(lstart, lstop, number)
    
    return np.exp(ldata)

if __name__ == '__main__':
    pass