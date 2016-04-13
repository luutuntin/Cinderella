#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement, division

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Demo:
>>>
...
['0.6', '0.@', '0.a', '0.b2', '0.f', '0.i', '0.m', '0.o', '0.p', '0.p2', '0.s', '0.t', '0.y', '1.a', '1.b2', '1.c2', '1.i', '1.s', '10.a', '10.a2', '10.c', '10.f', '10.h', '10.o', '11.d', '11.p', '12.c', '12.d', '12.e', '12.p', '13.a', '13.a2', '13.b2', '13.c', '13.c2', '13.c3', '13.c4', '13.d', '13.d3', '13.i3', '13.p', '13.p2', '13.p3', '13.s', '13.u', '14.a', '14.e', '14.n', '15.a', '15.a2', '15.a3', '15.a4', '15.a5', '15.a6', '15.b2', '15.c2', '15.d2', '15.d3', '15.g2', '15.g3', '15.h', '15.i2', '15.i4', '15.l', '15.l2', '15.o', '15.o2', '15.r', '15.t2', '15.t4', '15.t5', '16.6', '16.a', '16.c', '16.c2', '16.g', '16.m', '16.p', '16.p2', '16.t', '16.t2', '16.y', '17.a', '17.d', '17.f', '18.a', '18.a3', '18.a4', '18.b', '18.c', '18.e', '18.e2', '18.f', '18.t', '18.t2', '18.u', '19.a', '19.a2', '19.a3', '19.c', '19.c2', '19.l', '19.p', '19.p2', '2.b', '2.c', '2.d', '2.h', '2.t2', '20.a', '20.f', '20.o', '20.p2', '20.u', '20.v', '20.w', '21.c', '21.d', '21.g', '21.p', '21.s', '22.g', '22.k', '22.l', '22.n', '22.o', '22.s', '22.v', '23.c', '23.c2', '23.c3', '23.e', '23.g', '23.g2', '23.l', '23.m', '23.m2', '23.m3', '23.p', '23.t', '24.a', '24.d', '24.g', '24.g2', '24.l', '25.a', '25.c', '25.i2', '25.s', '25.t', '26.a', '26.i', '26.m2', '26.o2', '26.t', '26.t2', '26.t3', '27.a', '27.c', '27.e', '27.i2', '27.k', '27.m', '27.s', '27.s3', '27.s4', '27.t', '28.f', '28.interrogative', '28.t', '28.t2', '28.t4', '28.u2', '29.a', '29.c', '29.o', '29.s', '29.t', '3.c', '3.c2', '3.s', '3.s2', '3.w', '30.c2', '30.e', '30.o', '30.p', '30.p2', '30.s', '30.t', '30.t2', '31.b', '31.d', '31.h', '31.l', '32.a', '32.b', '32.g', '32.n2', '32.p', '32.t', '33.a', '33.g2', '33.m', '33.m2', '33.p', '33.s', '33.s2', '4.6', '4.a', '4.a2', '4.d', '4.m', '4.m2', '4.n', '4.p', '4.s', '4.t2', '4.t3', '5.a', '5.d', '5.j', '5.p', '5.t', '6.1', '6.a', '6.a2', '6.c', '6.d', '6.m', '6.o', '6.p', '6.s', '6.s2', '6.w', '7.i', '8.a', '8.a2', '8.d', '8.f', '8.g', '8.interrogative', '8.l', '8.s', '8.t', '9.a', '9.c', '9.f', '9.interrogative']
"""

#from semaland_anaphora_resolution import *
from semaland_linking_concept_definition import *

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


##def update_id_nodes(g,u,v):
##    """ """
##    g.node[u]['id_nodes'][v] = g.node[v]['content']

def id_nodes(g):
    """ """
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
                    #print(u)
    ##                if 'id_nodes' not in t.node[u]:
    ##                    t.node[u]['id_nodes'] = dict()
                    v = str(ld[i][k][0][1]) + '.' + \
                        ld[i][k][0][2]
                    #print(v)
    ##                update_id_nodes(t,u,v)
    ##                #t.node[u]['id_nodes'][v] = t.node[v]['content']
                    #t = nx.identified_nodes(t,u,v)
                    if v in t:
                        #t = nx.identified_nodes(t,u,v)
                        t = nx.identified_nodes(t,v,u)
                    else:
                        for n in id_nodes(t):
                            if v in t.node[n]['contraction']:
                                t = nx.identified_nodes(t,n,u)
##    for n in t:
##        if n.endswith('@'):
##            t.remove_node(n)
    t.remove_nodes_from([n for n in t
                         if n.endswith('@') and n!='0.@'])
    return t

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
    tg,ld = define_link_concepts(working_text,1)
    t = merge_id_nodes(tg,ld)
    print(sorted(t.nodes()))
    import matplotlib.pyplot as plt
    nx.draw_networkx(t)
    plt.show()
