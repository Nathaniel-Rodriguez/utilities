import numpy as np
from scipy.stats import bayes_mvs

def bayes_mvs_wrapper(sequence, alpha=0.9):

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

def estimate_beta_distribution_parameters(mean, variance):
    """
    Estimates the beta distribution alpha and beta parameters from the
    mean and variance of some data

    Note: for a beta distribution the mean is in [0, 1] and variance in [0, 0.5**2]
    Note: variance is bounded by mean: var <= mean * (1 - mean)
    """
    
    if (variance > 0.5**2) or (variance < 0.0):
        print("Warning! Variance out of bounds: [0, 0.5^2]")

    if (variance > (mean * (1. - mean))):
        print("Error! Variance larger than mean * (1 - mean). No beta distribution exists.")

    if (mean > 1.0) or (mean < 0.0):
        print("Warning! Mean out of bounds: [0, 1]")


    alpha = ((1. - mean) / variance - 1. / mean) * mean**2
    beta = alpha * (1. / mean - 1.)

    return alpha, beta

if __name__ == '__main__':
    pass