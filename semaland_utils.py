#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement

"""
cosi299a - Cinderella
alexluu@brandeis.edu
"""

from cPickle import dump, load, HIGHEST_PROTOCOL
import codecs

#https://github.com/tcurcuru/NLP4SLE/blob/master/nlp4sle_utilities.py
def read_lines(data_file):
    """ data file -> lines (strings) """
    with codecs.open(data_file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            yield line

def write_lines(lines,data_file):
    """ lines -> data file """
    with codecs.open(data_file,'w',encoding='utf-8') as f:
        for line in lines:
            f.write(line)

def save_data(data,pklfile_name):
    """ save data to a pickle file """        
    with open(pklfile_name,'wb') as f:
        dump(data,f,HIGHEST_PROTOCOL)

def load_data(pklfile_name):
    """ load data from a pickle file """        
    with open(pklfile_name,'rb') as f:
        data = load(f)
    return data

if __name__ == "__main__":
    pass

