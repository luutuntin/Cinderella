#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement, division

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Demo: (Cache size: 2)
>>> 
END OF FILE: chapter_01.txt
Cache size: 2
0 	 {}
0 	 {}
1 	 {'p': [(1.0, 0, 'p')]}
1 	 {'p': [(1.0, 0, 'p')]}
2 	 {'t': [(1.0, 1, 'p')]}
2 	 {'t': [(1.0, 1, 'p')]}
3 	 {'p': [(1.0, 1, 'a')], 'b': [(1.0, 1, 'b2')], 'b2': [(1.0, 0, 'b2')]}
3 	 {'p': [(1.0, 1, 'a')], 'b': [(1.0, 1, 'b2')], 'b2': [(1.0, 0, 'b2')]}
4 	 {'t': [(1.0, 3, 'b')]}
4 	 {'t': [(1.0, 3, 'b')]}
5 	 {'i': [(1.0, 0, 'i')]}
5 	 {'i': [(1.0, 0, 'i')]}
6 	 {'i': [(1.0, 5, 'i')]}
6 	 {'i': [(1.0, 5, 'i')], 't': [(1.0, 2, 't')]}
7 	 {'p': [(1.0, 6, 't')]}
7 	 {'p': [(1.0, 6, 't')]}
8 	 {'i': [(1.0, 7, 'p')], 't2': [(1.0, 7, 'p')], 'i2': [(1.0, 7, 'i')], 'm': [(1.0, 7, 'p')]}
8 	 {'i': [(1.0, 7, 'p')], 'm': [(1.0, 7, 'p')], 'i2': [(1.0, 7, 'i')], 't2': [(1.0, 7, 'p')]}
9 	 {'t': [(1.0, 8, 'g')]}
9 	 {'t': [(1.0, 8, 'g')]}
10 	 {}
10 	 {}
11 	 {'i': [(1.0, 8, 'i2')], 'h': [(1.0, 10, 'h')], 't': [(1.0, 8, 't2')]}
11 	 {'i': [(1.0, 8, 'i2')], 'h': [(1.0, 10, 'h')], 't': [(1.0, 8, 't2')]}
12 	 {'i': [(1.0, 11, 't')], 'b2': [(1.0, 4, 't')]}
12 	 {'i': [(1.0, 11, 't')], 'b2': [(1.0, 4, 't')]}
13 	 {'i': [(1.0, 11, 'i')], 'i2': [(1.0, 12, 'i')], 'g': [(1.0, 9, 't')]}
13 	 {'i': [(1.0, 11, 'i')], 'i2': [(1.0, 12, 'i')], 'i4': [(1.0, 12, 'i')], 'g': [(1.0, 9, 't')]}
14 	 {'t': [(1.0, 13, 'g')]}
14 	 {'t': [(1.0, 13, 'g')]}
15 	 {'i': [(1.0, 13, 'i')], 'p': [(1.0, 13, 'p2')], 't3': [(1.0, 13, 'p2')], 'g': [(1.0, 14, 't')]}
15 	 {'i': [(1.0, 13, 'i')], 'p': [(1.0, 13, 'p2')], 't3': [(1.0, 13, 'i4')], 'g': [(1.0, 14, 't')]}
16 	 {'i': [(1.0, 15, 'i')]}
16 	 {'i': [(1.0, 15, 'i')]}
17 	 {'i': [(1.0, 16, 'i')], 'p': [(1.0, 13, 'i2')], 'p2': [(1.0, 15, 'p')]}
17 	 {'i': [(1.0, 16, 'i')], 'p2': [(1.0, 15, 'p')], 'p': [(1.0, 15, 't3')]}
18 	 {'g': [(1.0, 15, 'g')]}
18 	 {'g': [(1.0, 15, 'g')]}
19 	 {'i': [(1.0, 17, 'i')]}
19 	 {'i': [(1.0, 17, 'i')]}
20 	 {'i': [(1.0, 19, 'i')], 'g': [(1.0, 15, 'g2')]}
20 	 {'i': [(1.0, 19, 'i')], 'g': [(1.0, 15, 'g2')]}
21 	 {'i': [(1.0, 20, 'i')]}
21 	 {'i': [(1.0, 20, 'i')]}
22 	 {}
22 	 {}
23 	 {'i': [(1.0, 21, 'i')]}
23 	 {'i': [(1.0, 21, 'i')]}
24 	 {'i': [(1.0, 23, 'i')]}
24 	 {'i': [(1.0, 23, 'i')]}
25 	 {'i': [(1.0, 24, 'i')], 't': [(1.0, 24, 'g')]}
25 	 {'i': [(1.0, 24, 'i')], 't': [(1.0, 23, 'p')]}
26 	 {'i2': [(1.0, 25, 'i')]}
26 	 {'i2': [(1.0, 25, 'i')]}
27 	 {'i': [(1.0, 26, 'i2')], 'p2': [(1.0, 17, 'p')], 't3': [(1.0, 26, 't2')]}
27 	 {'i': [(1.0, 26, 'i2')], 'p': [(1.0, 25, 't')], 'p2': [(1.0, 17, 'p')], 't3': [(1.0, 26, 't2')]}
28 	 {'i': [(1.0, 27, 'i')], 'p': [(1.0, 27, 'p')]}
28 	 {'i': [(1.0, 27, 'i')], 'p': [(1.0, 27, 'p')]}
29 	 {'h2': [(1.0, 11, 'h')], 'h': [(1.0, 28, 'p')], 's2': [(1.0, 28, 'p')]}
29 	 {'h2': [(1.0, 11, 'h')], 's2': [(1.0, 28, 'p')], 'h': [(1.0, 28, 'p')]}
30 	 {'i': [(1.0, 28, 'i')], 'p': [(1.0, 28, 'p')], 'b': [(1.0, 15, 'b2')], 'f': [(1.0, 5, 'j')]}
30 	 {'i': [(1.0, 28, 'i')], 'p': [(0.5, 29, 's2'), (0.5, 29, 'h')], 'b': [(1.0, 15, 'b2')], 'f': [(1.0, 5, 'j')]}
31 	 {'i': [(1.0, 30, 'i')]}
31 	 {'i': [(1.0, 30, 'i')]}
32 	 {'i': [(1.0, 31, 'i')], 'h': [(1.0, 31, 'h')]}
32 	 {'i': [(1.0, 31, 'i')], 'h': [(1.0, 31, 'h')]}
33 	 {'g': [(1.0, 32, 'h')], 'm2': [(1.0, 32, 'i')]}
33 	 {'g': [(1.0, 24, 'g')]}
R: 0.8966	P: 0.8667	F1: 0.8814


0 	 [(12.0, 'i'), (6.0, 'p')]
1 	 [(8.0, 'p'), (5.0, 'b2'), (4.0, 'a')]
2 	 [(6.333333333333333, 't2'), (4.5, 't')]
3 	 [(10.666666666666666, 'b'), (8.0, 'b2'), (6.666666666666666, 'p')]
4 	 [(20.666666666666668, 't')]
5 	 [(10.0, 'i'), (6.0, 'a')]
6 	 [(20.666666666666668, 'i'), (4.5, 't')]
7 	 [(8.0, 'p')]
8 	 [(12.666666666666666, 'i2'), (8.666666666666666, 'i'), (7.333333333333332, 'g'), (6.5, 't2'), (4.666666666666666, 'm')]
9 	 [(8.666666666666666, 't')]
10 	 [(8.0, 'o'), (8.0, 'h')]
11 	 [(8.5, 't'), (8.0, 'i'), (6.0, 'h')]
12 	 [(10.0, 'i'), (7.0, 'b2'), (4.0, 'e')]
13 	 [(12.0, 'i'), (9.333333333333334, 'g'), (5.333333333333333, 'i4'), (5.142857142857142, 'i2'), (4.0, 'p2'), (4.0, 'i3')]
14 	 [(10.0, 't')]
15 	 [(22.666666666666668, 'i'), (10.666666666666666, 'g'), (6.666666666666666, 'p'), (3.833333333333333, 't3'), (2.6666666666666665, 'a2'), (2.4761904761904763, 'h'), (2.4761904761904763, 'g3'), (2.4761904761904763, 'g2'), (2.4761904761904763, 'a5')]
16 	 [(10.666666666666666, 'i'), (4.666666666666666, 'c'), (3.0, 'p')]
17 	 [(8.0, 'i'), (4.0, 'p2'), (4.0, 'p')]
18 	 [(8.0, 'g'), (6.0, 'c'), (4.666666666666666, 'a3'), (4.0, 't2'), (4.0, 't')]
19 	 [(16.0, 'i'), (4.0, 'p'), (3.6, 'a3')]
20 	 [(12.666666666666666, 'i'), (4.666666666666666, 'g')]
21 	 [(12.666666666666666, 'i'), (4.666666666666666, 'c'), (4.0, 's')]
22 	 [(6.666666666666666, 'o'), (6.0, 'k'), (4.0, 'l')]
23 	 [(10.0, 'i'), (6.5, 'p'), (6.0, 'm3')]
24 	 [(10.0, 'i')]
25 	 [(10.0, 'i'), (8.0, 't'), (4.0, 'a')]
26 	 [(7.6, 'i2'), (5.166666666666666, 't3')]
27 	 [(19.333333333333336, 'i'), (7.5, 'p'), (4.933333333333334, 't3'), (4.0, 'p2')]
28 	 [(14.0, 'i'), (6.0, 'p')]
29 	 [(8.0, 's2'), (8.0, 'h'), (4.666666666666666, 'h2')]
30 	 [(10.0, 'i'), (5.333333333333333, 'p'), (4.666666666666666, 's'), (4.666666666666666, 'f'), (4.666666666666666, 'b')]
31 	 [(12.0, 'i'), (5.333333333333333, 'l'), (5.0, 'd')]
32 	 [(10.0, 'i'), (7.333333333333333, 'h'), (4.666666666666666, 'p'), (4.666666666666666, 'n2'), (4.666666666666666, 'g'), (4.666666666666666, 'b')]
33 	 [(8.666666666666666, 'g'), (4.333333333333333, 'm2')]
>>>
|| no givenness in salience factors
|||| cache size: 1 -> R: 0.8966	P: 0.8814	F1: 0.8889
|||| cache size: 3 -> R: 0.8966	P: 0.8525	F1: 0.8739
|||| cache size: 4 -> R: 0.8966	P: 0.8525	F1: 0.8739

1st and 2nd pronoun handling
antecas <-> 'conjunction'
edit semantic_match()
more for PREDICATE_NOUNS -> abandon
3 	 {..., 'b2': (1, set(['p']))} ->(0, set(['b2']))
vs
8 	 {'..., 'm': (7, set(['p'])), ...}
||and other semantic cases
add 'one' -> pronouns (in constant.py and pronouns.txt) ||22.o
remove deixis in ancas and antecas
3rd pronouns handling
update coref info
||previous stable version: 102
coref nodes handling
MUC
correct rank_ancas for the case of conjunction
"""

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

pros = dict()
for line in read_lines('Lists/pronouns.txt'):
    tokens = line.split()
    pro = dict()
    pro['num']=tokens[1]
    pro['gen']=tokens[2]
    pro['per']=tokens[3]
    pros[tokens[0]]=pro

def is_pronominal(g,n):
    """ 1/0 (True/False) """
    if g.node[n]['content'].ful_name_ in pros:
        return 1 # True
    return 0 # False

def is_pronominal_quote(g,n): # 1st and 2nd person pronouns
    """ 1/0 (True/False) """
    if g.node[n]['content'].ful_name_ in pros and \
       pros[g.node[n]['content'].ful_name_]['num'] in {1,2}:
        return 1 # True
    return 0 # False

def is_given(g,n): # node having at least one antecedent <- simplest
    """ 1/0 (True/False) """
    if 'coref' in g.node[n]:
        return 1 # True
    return 0 # False    

def classify_node(g,n): # g: AMR graph, n: AMR node
    """ -> '@', event, special concept, pronoun, conjunction, constant or other """
    if n=='@':
        return n
    node_concept = g.node[n]['content'].ful_name_
    if re.match(r'\S+-\d+',node_concept):
        return 'event' # node with sense tag
    if node_concept in AMR_SPECIAL_CONCEPTS:
        return 'special'
    if node_concept in NOMINATIVE_PRONOUNS:
        return 'pronoun'
    if node_concept in AMR_CONJUNCTIONS:
        return 'conjunction'
    if node_concept in DEIXIS:
        return 'deixis'
    if node_concept=='':
        return 'constant'
    return 'other' # named entities and abstract concepts???

def get_antecas(g): #antecas: antecedent candidates
    """ remove '@', events, special concepts, and constants """
    return set(n for n in g if classify_node(g,n) not in
               {'@','event','special','constant','conjunction','deixis'})

# assumption: the maximum number of arguments of a predicate < 10
l_re_in = r'^:ARG\d$'       # label pattern of core role in-edge
l_re_out = r'^:ARG\d-of$'   # label pattern of core role out-edge

def get_ancas(g): # g: AMR graph
    """ core roles or root node without sense tag """
    output = set()
    ns = set(n for n in g if classify_node(g,n) not in
             {'@','event','special','constant','deixis'})
    #for n in get_antecas(g):
    for n in ns:
        # root node, :ARGX, or :ARGX-of
        if '@' in g.predecessors(n) or \
           check_edge_label(g,n,'in',l_re_in) or \
           check_edge_label(g,n,'out',l_re_out): 
            output.add(n)
    for n in output:
        if is_pronominal_quote(g,n):
            output.remove(n)
    return output

def update_frequency(g,n,e_di,l_re): #assumption: existence of edges
    """ -> number of instances of each core role type a node plays """
    #output = defaultdict(int)
    output = dict()
    for e in get_edges_by_direction(g,n,e_di):
        if 'label' in e[2] and re.match(l_re,e[2]['label']):
            arg_index = e[2]['label'][4]
            if arg_index in output:
                output[arg_index] += 1
            else:
                output[arg_index] = 1
    return output

def update_frequency_ext(g,n,e_di,l_re,conj): # extended for conjunction case
    """ ... """
    if conj:
        output = dict()
        freq_n = update_frequency(g,n,e_di,l_re)
        keys_n = set(freq_n.keys())
        freq_conj = update_frequency(g,conj,e_di,l_re)
        keys_conj = set(freq_conj.keys())
        for i in keys_n.intersection(keys_conj):
            output[i] = freq_n[i] + freq_conj[i]
        for i in keys_n.difference(keys_conj):
            output[i] = freq_n[i]
        for i in keys_conj.difference(keys_n):
            output[i] = freq_conj[i]
        return output
    
    return update_frequency(g,n,e_di,l_re)

#def get_salience_factors(g,n):
def get_salience_factors(g,n,conj=None):
    # g: AMR graph, n: AMR node
    """ distance from graph root, core roles, pronominalization, giveness """
    output = dict()
    output['dis'] = nx.shortest_path_length(g,'@',n)
    #output['in'] = update_frequency(g,n,'in',l_re_in)
    output['in'] = update_frequency_ext(g,n,'in',l_re_in,conj)
    #output['out'] = update_frequency(g,n,'out',l_re_out)
    output['out'] = update_frequency_ext(g,n,'out',l_re_out,conj)
    output['pro'] = is_pronominal(g,n)
    output['giv'] = is_given(g,n)
    return output    

def score_core_roles(s_factors,e_di):
    """ smaller index, better score """
    output = float()
    for k in s_factors[e_di]:
        output += s_factors[e_di][k]/(int(k) + 1)
    return output

# SALIENCE formula
def salience(s_factors,w_dis,w_in,w_out,w_pro,w_giv): # recency excluded -> cache model
    """ -> salience score """
    output = sum([
        w_dis/s_factors['dis'],
        w_in*score_core_roles(s_factors,'in'),
        w_out*score_core_roles(s_factors,'out'),
        w_pro*s_factors['pro'],
        w_giv*s_factors['giv'],
        ])
    return output


#coreference chains and links
def update_coref_chains(text,i,ni,j,nj,wij):
    # text: list of AMR graphs
    # i/j: index of AMR graph containing anaphor ni/ antecedent nj
    # wij: weight of coreference link between ni and nj
    """ -> updated AMR text with coreference information """
    if 'coref' not in text[i].node[ni]:
        text[i].node[ni]['coref'] = list() # cannot be set()
        # because components' type is 'list' (unhashable)
    coref_link = (wij,j,nj)
    if 'coref' in text[j].node[nj]:
        for chain in text[j].node[nj]['coref']:
            chain.insert(0,coref_link)
            text[i].node[ni]['coref'].append(chain)
    else:
        text[i].node[ni]['coref'].append([coref_link])
        
def update_coref_links(link_dict,i,ni,j,nj,wij):
    # link_dict: default dict of resolved coreference links
    # i/j: index of AMR graph containing anaphor ni/ antecedent nj
    # wij: weight of coreference connection between ni and nj
    """ -> updated AMR text with coreference information """
    coref_link = (wij,j,nj)
    if ni in link_dict[i]:
        link_dict[i][ni].append(coref_link)
    else:
        link_dict[i][ni] = [coref_link]


def define_cache(text,cache_size,i):
    # text: list of AMR graphs, i: index of current AMR graph
    """ -> lists of indexes of  graphs in / out of cache"""
    if i>0:
        if i>cache_size:
            cache = [(i-x-1) for x in range(cache_size)]
            non_cache = range(i-cache_size-1,-1,-1)
        else:
            cache = range(i-1,-1,-1)
            non_cache = None
        return cache, non_cache
    return None
        
def rank_ancas(g):
    """ """
    output = dict()
    ancas = get_ancas(g)
    s_factors = dict()
    for n in ancas:
        if classify_node(g,n)!='conjunction':
            output[n] = salience(get_salience_factors(g,n),
                                 8,4,1,2,1)
        else:
            temp = set()
            for nn in g.node[n]['content'].next_:
                if re.match(l_re_op,nn.edge_label_) and \
                   (classify_node(g,nn.name_) not in \
                    {'event','special','constant'}):
                    temp.add(nn.name_)
            for nnn in temp:
                #output[nnn] = salience(get_salience_factors(g,nnn),
                output[nnn] = salience(get_salience_factors(g,nnn,n),
                                       8,4,1,2,1)
    return output

def new_concept(node):# node: node structure of amr_reader
    """ -> 'sure'/'unsure' """
    for next_node in node.next_:
        if (next_node.edge_label_==':mod' and \
           next_node.ful_name_ in {'another','any','some'}) or \
           (next_node.edge_label_==':quant' and \
           (next_node.ful_name_ in {'many','much','lot','few','little'} or \
            alnum_is(next_node.ful_name_)=='d')):
            return 'sure'
    return 'unsure'

def ne_constraint(n1,n2): # ne: named entity
    """ -> passed/failed """
    if n1.is_entity_ and n2.is_entity_ and \
       n1.entity_name_!=n2.entity_name_:# <-> string match
        return 'failed'
    return 'passed'
    
def string_match(anca_node,text,i,m_function,m_value,link_dict):
    # m_function/m_value: matching function/value
    """ -> set of antecas string-matching anca """
    output = set()
    if new_concept(anca_node)=='sure' or \
       anca_node.ful_name_=='thing': # anca_node.ful_name_ in PREDICATE_NOUNS
        return output
    g = text[i]
    ranked_ancas = rank_ancas(g)
    antecas = get_antecas(g)
    for n in antecas:
        n_node = g.node[n]['content'] 
        n_str = n_node.ful_name_
        if n_str in {'he','she','it','they'}:
            for cn in get_coref_nodes(text,i,n,link_dict):
                cn_node = text[cn[0]].node[cn[1]]['content']
                cn_str = cn_node.ful_name_
                if cn_str!=n_str: # not pronominal
                    n_str = cn_str
                    n_node = cn_node
                    break                    
        if m_function(anca_node.ful_name_,n_str)==m_value and \
           ne_constraint(anca_node,n_node)=='passed':
            output.add(n)
    #if any((n in ancas) for n in matched):
    if output.intersection(ranked_ancas):
        output = output.intersection(ranked_ancas)
        if len(output)>1:
            highest = max(ranked_ancas[n] for n in output)
            output = set(n for n in output if ranked_ancas[n]==highest)
    return output

def semantics_of_node(node):
    """ -> set of node name(s) and the corresponding POS"""
    output = set()
    #if node.ful_name_ not in PREDICATE_NOUNS:
    if node.ful_name_!='thing':
        pos = POS_SET
        output.add(node.ful_name_)
    else:
        pos = {'v'}
        for next_node in node.next_:
            if re.match(l_re_out,next_node.edge_label_):
##            if (node.ful_name_=='thing' and \
##                next_node.edge_label_==':ARG1-of') or \
##               (node.ful_name_!='thing' and \
##                next_node.edge_label_==':ARG0-of'):
                output.add(next_node.ful_name_.split('-')[0]) # event
    return output.difference(NOMINATIVE_PRONOUNS),pos

def get_sense_index_sum(pair): # pair: output of get_best_synset_pair()
    """ -> sum of sense indexes of two synsets in the pair """
    output = int()
    for s in pair[0]:
        output += int(s.name().split('.')[-1])
    return output    

def semantic_match(anca_node,text,i,
                   threshold,delta,sem_depth,sense_index_sum,
                   link_dict):
    # anca_node: node structure of amr_reader
    """ -> set of node names """
    output = set()
    if new_concept(anca_node)=='sure':
        return output
    words1,pos1 = semantics_of_node(anca_node)
    words2,pos2 = set(),set()
    g = text[i]
    ranked_ancas = rank_ancas(g)
    antecas = get_antecas(g)
    for n in antecas:
        n_node = text[i].node[n]['content']
        if n_node.ful_name_ in {'he','she','it','they'}:
            for cn in get_coref_nodes(text,i,n,link_dict):
                cn_node = text[cn[0]].node[cn[1]]['content']
                if cn_node.ful_name_!=n_node.ful_name_: # not pronominal
                    words2,pos2 = semantics_of_node(cn_node)
                    break
        else:            
            words2,pos2 = semantics_of_node(n_node)
        for w1 in words1:
            for w2 in words2:
##                if gender_constraint(w1,w2)=='passed' and \
##                   animacy_constraint(w1,w2)=='passed':
                if gender_constraint(w1,w2)=='passed' or \
                   animacy_constraint(w1,w2)=='passed':
                    semantic_pair = get_best_synset_pair(w1,w2,pos1,pos2)
                    temp_sim = threshold # lch_similarity
                    temp_dep = 3 # min_depth <- hard code
                    temp_sum = sense_index_sum
                    if pos1=={'v'} or pos2=={'v'} or \
                       (semantic_pair and semantic_pair[3] and \
                        semantic_pair[3]>sem_depth):
                        temp_sim = threshold - delta
                        temp_dep = 0 # <- hard code
                    if pos1=={'v'} or pos2=={'v'} or \
                       animacy(w1).intersection(w2)!=set():
                        temp_sum = sense_index_sum + 6 # bonus <- hard code
                    if semantic_pair and semantic_pair[1]>=temp_sim and \
                       semantic_pair[3] and semantic_pair[3]>temp_dep and \
                       ne_constraint(anca_node,n_node)=='passed' and \
                       get_sense_index_sum(semantic_pair)<=temp_sum:
                        output.add((semantic_pair[1],n_node.name_))
    if output:
        best_sem_sim = max(output)[0]
        output = set(e[1] for e in output if e[0]==best_sem_sim)
    if output.intersection(ranked_ancas):
        output = output.intersection(ranked_ancas)
        if len(output)>1:
            highest = max(ranked_ancas[n] for n in output)
            output = set(n for n in output if ranked_ancas[n]==highest)
    return output

def resolve_pro(p_node,g,threshold): # p_node: node of 3rd pronoun
    """ -> set of node names """
    ranked_ancas = rank_ancas(g)
    temp = [(n,r) for (n,r) in sorted(ranked_ancas.items(),
                                      key=itemgetter(1),reverse=True)
               if r>=threshold and \
                  not((g.node[n]['content'].ful_name_ in \
                       NOMINATIVE_PRONOUNS.difference({'one'})) and \
                      g.node[n]['content'].ful_name_!=p_node.ful_name_) and \
                  gender_constraint_pro(p_node.ful_name_,
                      g.node[n]['content'].ful_name_)=='passed' and \
                  animacy_constraint_pro(p_node.ful_name_,
                      g.node[n]['content'].ful_name_)=='passed']
    if not temp:
        output = set(n for n in get_antecas(g).difference(ranked_ancas)
                       if g.node[n]['content'].ful_name_==p_node.ful_name_)
        return output
    output = set(n for n,r in temp if r==temp[0][1])
    return output

def get_coref_nodes(text,i,n,link_dict):
    """ """
    output = list()
    if (i in link_dict) and \
       (n in link_dict[i]) and \
       len(link_dict[i][n])==1:
        ante = link_dict[i][n][0][1:]
        output.append(ante)
        output.extend(get_coref_nodes(text,ante[0],ante[1],link_dict))
    return output

def resolve_anca(n,i,text,cache_info,link_dict):
    """ -> set of matched nodes """
    matched = set()
    threshold =[2.7,3.5]
    sem_depth = [5,3]
    sense_index_sum = [2,4]
    n_node = text[i].node[n]['content']
    if classify_node(text[i],n)=='other':        
        for p in range(len(cache_info)):
            if cache_info[p]: # for non_cache partition
                for j in cache_info[p]:
                    matched = string_match(n_node,text,j,
                              truecase_matching_is,'f',link_dict)
                    if matched:
                        matched = (j,matched)
                        break
                    else:
                        matched = semantic_match(n_node,text,j,
                                  threshold[p],0.6,sem_depth[p],
                                  sense_index_sum[p],link_dict)
                        if matched:
                            matched = (j,matched)
                            break
            if matched:
                break
    elif n_node.ful_name_ in {'i','we','you',"y'all"}:
        for j in range(i-1,-1,-1):
            matched = string_match(n_node,text,j,
                      truecase_matching_is,'f',link_dict)
            if matched:
                matched = (j,matched)
                break
    elif n_node.ful_name_ in {'he','she','it','they'}:
        for j in cache_info[0]:
            matched = resolve_pro(n_node,text[j],6.0)
            if matched:
                matched = (j,matched)
                break    
    return matched

l_re_op = r'^:op\d+$'
#def resolve_ancas_graph(i,text,cache_size):
def resolve_ancas_graph(i,text,cache_size,link_dict):
    """ -> dict whose keys are ancas and whose values are sets of antecas"""
    output = dict()
    cache_info = define_cache(text,cache_size,i)
    if cache_info:
        ranked_ancas = [n for n,_ in sorted(rank_ancas(text[i]).items(),
                                            key=itemgetter(1),
                                            reverse=True)]
        for n in ranked_ancas:
            output[n] = resolve_anca(n,i,text,cache_info,link_dict)
            if output[n]:
                w = 1/(len(output[n][1])) # weight of coref link
                for m in output[n][1]:
                    update_coref_chains(text,i,n,output[n][0],m,w) # <- this change rank values??? (<-> giveness???)
                    update_coref_links(link_dict,i,n,output[n][0],m,w)
    return output    
    
def resolve_ancas_text(text,cache_size):
    """ -> output (legacy) and link dict (key info) """
    output = dict()
    link_dict = dict()
    for i in range(len(text)):
        link_dict[i] = dict()
        output[i] = resolve_ancas_graph(i,text,cache_size,link_dict)
    return output,link_dict

def get_gold(f): # f: xml file of anaphora resolution annotation
    """ -> gold link dict """
    output = dict()
    tree = ET.parse(f)
    for (i,amr) in enumerate(tree.findall('./sntamr/amr')[1:]):
        output[i] = dict()
        if 'ana' in amr.attrib:
            for link in amr.attrib['ana'].split():
                n,jm = link.split(':')
                j,m = jm.split('.')
                output[i][n] = [(1.0,int(j)-2,m)]
    return output

def muc(gold_dict,test_dict):
    """ -> MUC F-measure """
    gold = float()
    test = float()
    correct = float()
    for i in gold_dict:
        gold += len(gold_dict[i])
        test += len(test_dict[i])
        for n in test_dict[i]:
            if n in gold_dict[i]:
                for l in test_dict[i][n]:
                    if l[1:]==gold_dict[i][n][0][1:]:
                        correct += l[0]
    print(gold,test,correct)
    r = correct/gold # recall
    p = correct/test # precision
    f1 = 2*r*p/(r+p)
    return r,p,f1
    

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
    print('Cache size: 2')
    output,link_dict = resolve_ancas_text(working_text,2)

##    for  in output:
##        print(i,'\t',output[i])

##    print('\n')

    gold_dict = get_gold(DATA_AMR_ANNOTATED_LPP_01)

    for i in gold_dict:
        print(i,'\t',gold_dict[i])
        print(i,'\t',link_dict[i])
    r,p,f1 = muc(gold_dict,link_dict)
    print("R: {0:.4f}\tP: {1:.4f}\tF1: {2:.4f}".format(r,p,f1))

    print('\n')

##    ranked_ancas = [rank_ancas(g) for g in working_text]
##    for i in range(len(ranked_ancas)):
##        temp = sorted([(v,k) for (k,v) in ranked_ancas[i].items()],
##                      reverse=True)
##        print(i,'\t',temp)
