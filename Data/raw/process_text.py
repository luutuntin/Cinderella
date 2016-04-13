# -*- coding: utf-8 -*-

from __future__ import with_statement
import codecs
import os
from os.path import join

def read_text(file_name):
    """ txt file -> string """
    with codecs.open(file_name,'r','utf-8') as f:
        return f.read()

def write_text(text,file_name):
    """ string -> txt file """
    with codecs.open(file_name,'w','utf-8') as f:
        f.write(text)

def fix_text(indir,outdir,file_name):
    """ txt file -> fixed txt file """
    text = read_text(indir+'/'+file_name).replace('\r','')
    write_text(text,outdir+'/'+file_name)

def get_files(indir):
    """ -> list of paths to txt files in the corpus """
    output = list()
    for _,_,files in os.walk(indir):
        output.extend(files)
    return sorted(output)

def fix_texts(indir,outdir):
    """ txt files -> fixed txt files """
    files = get_files(indir)
    for f in files:
        if f[-4:]=='.txt':
            fix_text(indir,outdir,f)

if __name__ == "__main__":
    #fix_texts('original','processed')
    pass
