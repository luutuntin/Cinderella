#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement, division

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Demo:
...
"""

from semaland_anaphora_resolution import *

from constants import *
from semaland_utils import *
from semaland_amr_graph import *
from semaland_semantic_features import *
from semaland_string_features import *
import networkx as nx
import re
from collections import defaultdict
import xml.etree.ElementTree as ET
from operator import itemgetter
from copy import deepcopy


def add_sent_id(t): # t: AMR text
    """ add sentence ID to node labels ('x' -> 'i.x') """
    for i in range(len(t)):
        mapping = dict(zip(t[i].nodes(),
                  [str(i)+'.'+l for l in t[i].nodes()]))
        t[i] = nx.relabel_nodes(t[i],mapping)


def get_gold_edited(f): # f: xml file of anaphora resolution annotation
    """ -> gold link dict """
    output = dict()
    tree = ET.parse(f)
    for (i,amr) in enumerate(tree.findall('./sntamr/amr')[1:]):
        output[i] = dict()
        if 'ana' in amr.attrib:
            for link in amr.attrib['ana'].split():
                n,jm = link.split(':')
                j,m = jm.split('.')
                #output[i][n] = [(1.0,int(j)-2,m)]
                output[i][n] = [(1.0,int(j)-2,str(int(j)-2)+'.'+m)]
    return output

def define_link_concepts(t,c): # t: AMR text, c: cache size
    """ -> AMR text with sentence-identified nodes and link dict """
    _,ld = resolve_ancas_text(t,c) # ld: link dict
    add_sent_id(t)
    return t,ld
    

def main():
    """ """
    pass

if __name__ == "__main__":
    #main()
    amr_table = get_amr_table_path(DATA_AMR_LPP_01)
    docid = 'lpp_1943'
    doc = amr_table[docid]
    annotated_doc = ET.parse(DATA_AMR_ANNOTATED_LPP_01)
    quote_info = [('quote' in amr.attrib)
                  for amr in annotated_doc.findall('./sntamr/amr')]
    text = [AMRGraph(sen=doc[k],quote=quote_info[k-1]) # doc index starting at 1
            for k in sorted(doc.keys())]
    text[4].add_edge('c2','b',label=':ARG0')
    text[4].add_edge('c2','p',label=':ARG1')
    # http://www.nltk.org/book/ch04.html
    working_text = deepcopy(text[1:])
    print('Cache size: 1')
##    output,link_dict = resolve_ancas_text(working_text,1)
##
####    for  in output:
####        print(i,'\t',output[i])
##
####    print('\n')
##
##    gold_dict = get_gold(DATA_AMR_ANNOTATED_LPP_01)
##    #gold_dict = get_gold_edited(DATA_AMR_ANNOTATED_LPP_01)
##
##    for i in gold_dict:
##        print(i,'\t',gold_dict[i])
##        print(i,'\t',link_dict[i])
##    r,p,f1 = muc(gold_dict,link_dict)
##    print("R: {0:.4f}\tP: {1:.4f}\tF1: {2:.4f}".format(r,p,f1))
##
##    print('\n')
##
####    ranked_ancas = [rank_ancas(g) for g in working_text]
####    for i in range(len(ranked_ancas)):
####        temp = sorted([(v,k) for (k,v) in ranked_ancas[i].items()],
####                      reverse=True)
####        print(i,'\t',temp)
##
##    
##    add_sent_id(working_text)
    t,ld = define_link_concepts(working_text,1)
