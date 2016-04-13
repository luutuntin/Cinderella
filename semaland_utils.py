#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement

"""
cosi299a - Cinderella
alexluu@brandeis.edu
"""

def read_lines(data_file):
    """ data file -> lines (lists) """
    with open (data_file,'r') as f:
        for line in f.readlines():
            yield line

if __name__ == "__main__":
    pass

