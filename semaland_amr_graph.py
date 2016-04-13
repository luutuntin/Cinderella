#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Quote consideration
"""

#from amr_common.AMRGraph import AMR
from amr_reader.src.amr import get_amr_table_path
import networkx as nx
import re
from constants import *
import xml.etree.ElementTree as ET

class AMRGraph(nx.MultiDiGraph):
    """
    Interested operations: graph union, vertex identification
    Add node/edge attributes: entry id, frequency
    """
    def __init__(self, data=None, sen=None, quote=False):
        super(AMRGraph, self).__init__(data)
        self.quote = quote
        if sen!=None:
            # use sen.amr_nodes_ and sen.graph_
            nodes = set()
            for e in sen.graph_:
                self.add_edge(e[0], e[1], label=str(e[2]))
                nodes.add(e[0])
                nodes.add(e[1])
            for n in nodes:
                if n != '@':
                    self.node[n]['content'] = sen.amr_nodes_[n]

def get_edges_by_direction(g,n,e_di):
    # g: AMR graph, n: node, e_di: 'in'/'out'
    """ -> incoming/outgoing edges of node in graph """
    if e_di=='in':
        return g.in_edges(n,data=True)
    elif e_di=='out':
        return g.out_edges(n,data=True)
    else:
        print('Invalid e_di info!')
        return None
        
def check_edge_label(g,n,e_di,l_re):
    # g: AMR graph, n: node, e_di: 'in'/'out', l_re: label pattern
    """ -> True/False (whether there is an edge matching l_re) """
    edges = get_edges_by_direction(g,n,e_di)
    if not edges:
        return None
    else:
        for e in edges:
            if 'label' in e[2]: # e[2] is dict of edge attribute
                if re.match(l_re,e[2]['label']):
                    return True
    return False

##def integerize_senids(amr_table): #-> fixed in amr-reader (reader.py -> main())
##    """ Fix ordering problem of amr-reader """
##    output = dict() #new amr_table with fixed sentence order
##    for docid in amr_table:
##        temp = dict()
##        for senid in amr_table[docid]:
##            senid_int = int(senid[len(docid)+1:])
##            temp[senid_int] = amr_table[docid][senid]
##            temp[senid_int].senid_ = senid_int
##        output[docid] = temp
##    return output
        
if __name__ == "__main__":
    #pass
    amr_table = get_amr_table_path(DATA_AMR_LPP_01)
    docid = 'lpp_1943'
    doc = amr_table[docid]
    annotated_doc = ET.parse(DATA_AMR_ANNOTATED_LPP_01)
    quote_info = [('quote' in amr.attrib)
                  for amr in annotated_doc.findall('./sntamr/amr')]
    #text = [AMRGraph(sen=s) for _,s in sorted(doc.items())]
    text = [AMRGraph(sen=doc[k],quote=quote_info[k-1]) # doc index starting at 1
            for k in sorted(doc.keys())]
    text[4].add_edge('c2','b',label=':ARG0')
    text[4].add_edge('c2','p',label=':ARG1')
    
