import numpy as np

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