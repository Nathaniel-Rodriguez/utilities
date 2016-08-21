"""
This file contains file I/O functions. Currently it includes the following:

readcol
    Reads columns from a file.
 
writecol
    Writes to file a list of columns provided as arguments to the function.

load_object
    loads a pickled python object from file

save_object
    saves a python object to file by pickling it

"""

import os
import sys
import pickle

def readcol(filename,format='s',delimiter=None,col=None,skiplines=[]):
    """
    readcol(filename,format='s',delimiter=None,col=None,skiplines=[])

    Reads columns from a file.
    
    filename 
        filename of input file
    format 
        string of format characters (auto formats output)
        s - string
        i - int
        f - float
        Letters must be chosen in the format of a string for each
        column to be output. The default setting for format is 's'.
    delimiter 
        char used to separate columns in a line of text. If None is
        chosen then the full line of a file will be read in.
    col 
        can optionally list the columns you want to return (list of ints).
        By default col=None which means that all columns will be read if
        a delimiter is chosen, or only one if no delimiter is chosen.
    skiplines 
        list of lines to skip in reading.
    
    Returns lists. When multiple columns are chosen the function returns
    each one in the order provided in the col argument. If no col argument was
    given, yet all the columns were read, then a single list containing all the 
    columns is returned.
    
        example: firstcol, secondcol, thrdcol = readcol(file,'sif',',',[1,2,3])
    or
        example cols = readcol(file,'s',',')
    
    """

    # Reject bad input
    if  (delimiter == None) and (col != None): 
        if (len(format) == len(col)):
            sys.exit("Must have delimiter for multiple columns.")

    # Open file and read lines into variables.
    if os.path.exists(filename):
        infile = open(filename,'r')
    else:
        sys.exit("The file named: " + filename + " does not exist.")
    
    # Default read all columns as a single format
    # This requires a delimiter to be defined, col set to None
    if (delimiter != None) and (col == None) and (len(format) == 1):
        data = []
        for i,line in enumerate(infile.readlines()):
            if (i+1 in skiplines) == False: 
                fields = line.strip().split(delimiter)
                fields = [field for field in fields if field != ""]
                row = []
                for str in fields:
                    row.append(str)
                data.append(row)
        # Put row values into their respective columns
        columns = zip(*data)
        
        if len(columns) == 1:   
            # Format data 
            col_list = list(columns[0])
            type = format[0]
            if type == 'i':
                col_list = [int(val) for val in col_list]
            elif type == 'f':
                col_list = [int(val) for val in col_list]
            elif type != 's':
                sys.exit("Warning: Unrecognized type " + type + " chosen!")    
            return col_list
        else:
            # Format data
            col_list = [list(tupl) for tupl in columns]
            type = format[0]
            if type == 'i':
                col_list = [map(int,col) for col in col_list]
            elif type == 'f':
                col_list = [map(float,col) for col in col_list]
            elif type != 's':
                sys.exit("Warning: Unrecognized type " + type + " chosen!")    
            return col_list 
        
    # Read a single column file
    # This requires the delimiter to be set to None, and col to be set to None
    # Only the first format character is used for formating, all others are 
    # ignored
    elif (delimiter == None) and (col == None):
        data = []
        for i,line in enumerate(infile.readlines()):
            if (i+1 in skiplines) == False: 
                field = line.strip()
                data.append(field)
                
        # Format data 
        type = format[0]
        if type == 'i':
            data = map(int,data)
        elif type == 'f':
            data = map(float,data)
        elif type != 's':
            sys.exit("Warning: Unrecognized type " + type + " chosen!")    
        return data
    
    # Read multicolumn file with different formats for the first N columns
    # where N is the number of format options chosen
    # This requires a delimiter to be set and col to be set to None
    elif (delimiter != None) and (col == None) and (len(format) > 1):
        data = [[] for dummy in range(len(format))]
        for i,line in enumerate(infile.readlines()):
            if (i+1 in skiplines) == False: 
                fields = line.strip().split(delimiter)
                fields = [field for field in fields if field != ""]
                for j,val in enumerate(fields):
                    try:
                        data[j].append(val)
                    except IndexError:
                        pass
    
    # Read multicolumn file with different formats for specific columns
    # This requires a delimiter to be set and col to be set
    # Col must be the same length as format 
    # *there is no difference between reading a single column with col set
    #  and having default col with no delimiter set 
    elif (delimiter != None) and (col != None):
        data = [[] for dummy in range(len(format))]
        assert(len(col) == len(format))
        for i,line in enumerate(infile.readlines()):
            if (i+1 in skiplines) == False: 
                fields = line.strip().split(delimiter)
                fields = [field for field in fields if field != ""]
                for j in range(len(col)):
                    try:
                        data[j].append(fields[col[j]-1])
                    except IndexError:
                        pass
    
    # Read 
    else:
        sys.exit("Error: Inappropriate input provide.")
                    
    infile.close()
        
    # Format data        
    for i,type in enumerate(format):
        if type == 'i':
            data[i] = map(int,data[i])
        elif type == 'f':
            data[i] = map(float,data[i])
        elif type != 's':
            sys.exit("Warning: Unrecognized type " + type + " chosen!")
    
    # Convert to tuple 
    if len(data) == 1:
        columns = tuple(data[0])
    else: 
        columns = tuple(data)
    
    return columns

def writecol(filename,delimiter,firstline,*args):
    """
    writecol(filename,delimiter,firstline,*args)

    Writes to file a list of columns provided as arguments to the function.
    If input is provided for firstline that is not "", then that string
    is made the first line of the file. Columns must be of same length 
    
    filename
        file to be read
    delimiter
        character or characters used as a delimiter between columns
    firstline
        header for file, if set to '', then none is written
    *args
        lists of columns to be written to the text file
    
    """
    
    col = [arg for arg in args]
    
    # Make sure columns are of the same length
    for x in col:
        assert(len(x) == len(col[0]))
    
    lines = []
    if firstline != "":
        lines.append(firstline + '\n')
    
    col_num = range(0,len(col))
    end = col_num[-1]
    for i in range(0,len(col[0])):
        line = ''
        for j in col_num:
            if j == end:
                line += str(col[j][i])
            else:
                line += str(col[j][i]) + delimiter
        line += '\n' 
        lines.append(line)
    
    outfile = open(filename,'w')
    outfile.writelines(lines)
    outfile.close()

def save_object(obj, filename):
    """
    Save an object to file for later use.
    """
    
    file = open(filename, 'wb')
    pickle.dump(obj, file)
    file.close()

def load_object(filename):
    """
    Load a previously saved object.
    """
    
    file = open(filename, 'rb')
    return pickle.load(file)

if __name__ == "__main__":
    pass
