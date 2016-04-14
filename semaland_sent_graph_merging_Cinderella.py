#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement, division

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Demo:

"""

#from semaland_linking_concept_definition import *
from semaland_linking_concept_definition_Cinderella import *

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
import matplotlib.pyplot as plt


def id_nodes(g): # g: AMR graph (in merging process)
    """ -> list of identified nodes in g"""
    return [n for n in g if 'contraction' in g.node[n]]


def merge_id_nodes(tg,ld): # tg: sentence-level AMR graphs for text, ld: link dict
    """ -> t: document-level AMR graph for text """
    t = AMRGraph()    
    for i in range(len(tg)):
        t = nx.union(t,tg[i])
        if not ld[i]:
            t = nx.identified_nodes(t,'0.@',str(i)+'.@')
        else:
            for k in ld[i]:
                if len(ld[i][k])==1:
                    u = str(i) + '.' + k
                    v = str(ld[i][k][0][1]) + '.' + \
                        ld[i][k][0][2]
                    if v in t:
                        t = nx.identified_nodes(t,v,u)
                    else:
                        for n in id_nodes(t):
                            if v in t.node[n]['contraction']:
                                t = nx.identified_nodes(t,n,u)
    t.remove_nodes_from([n for n in t
                         if n.endswith('@') and n!='0.@'])
    return t

def draw_graph(g):
    """ using matplotlib.pyplot """    
    nx.draw_networkx(g)
    plt.show()

def main():
    """ """
    pass

if __name__ == "__main__":
    #main()
    amr_table = get_amr_table_path(DATA_AMR_EDITED)
    docids = ['Ariel','Aurora','Belle','Cinderella','Snow_White']
    text = dict()
    print('Cache size: 1')
    tg = dict()
    ld = dict()
    t = dict()
    for docid in docids:
        print(docid)
        text[docid] = [AMRGraph(sen=s) for _,s in sorted(amr_table[docid].items())]        
        tg[docid],ld[docid] = define_link_concepts(text[docid],1)
        t[docid] = merge_id_nodes(tg[docid],ld[docid])
        draw_graph(t[docid])
