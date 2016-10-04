import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def ecdf(data):
    
    data = np.sort(data)
    size = float(len(data))
    all_unique = not( any( data[:-1]==data[1:] ) )
    if all_unique:
        cdf = np.array([ i / size for i in range(0,len(data)) ])
    else:
        cdf = np.searchsorted(data, data,side='left')/size
        unique_data, unique_indices = np.unique(data, return_index=True)
        data=unique_data
        cdf = cdf[unique_indices]

    return data, cdf

def eccdf(data):

    sorted_data, cdf = ecdf(data)
    return sorted_data, 1. - cdf

def plot_ccdf(prefix, data, xlabel='', x_log=False, y_log=False):

    x, y = eccdf(data)
    plt.clf()
    plt.plot(x, y, 'bo')
    if x_log == True: plt.xscale('log')
    if y_log == True: plt.yscale('log')
    plt.ylabel('CCDF')
    plt.xlabel(xlabel)
    plt.savefig(prefix + '.png', dpi=300)
    plt.clf()
    plt.close()

def generate_color(index, loop_size=12, colormap=cm.Set1):
    """
    """

    return colormap((index%12 + index/12)*256 / loop_size)

if __name__ == '__main__':
    pass