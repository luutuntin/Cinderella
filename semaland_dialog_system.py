#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, with_statement, division

"""
cosi299a- Cinderella
alexluu@brandeis.edu

Note:
n/c: interchangeable nodes/concept nodes

Demo:

"""

from semaland_sent_graph_merging_Cinderella import *
from random import choice
from semaland_utils import *
from nltk import FreqDist
import nltk
wnl = nltk.WordNetLemmatizer()

def top_k(t,k): # t: document-level AMR graph of text
    """ -> top k most frequent identified nodes in t """
    return sorted([(len(t.node[n]['contraction']),n)
                   for n in id_nodes(t) if n!='0.@'],
                  reverse=True)[:k]

def node_concept(n): # n: AMR node
    """ -> node concept and respective category ('n'/'a'/'p') """
    if n['content'].is_entity_:
        return (n['content'].entity_name_,'n')
    elif n['content'].ful_name_ in pros:
        return (n['content'].ful_name_,'p')
    # abstract concept
    return (n['content'].ful_name_,'a')

def node_semantics(n): # n: AMR node
    """ -> dict of three semantic categories: 'n', 'a', 'p' """
    temp = defaultdict(list)
    nc = node_concept(n)
    temp[nc[1]].append(nc[0])
    
    if 'contraction' in n:
        for nn in n['contraction']:
            nnc = node_concept(n['contraction'][nn])
            temp[nnc[1]].append(nnc[0])

    for i in range(len(temp['a'])):
        for n in set(temp['n']):
            if lowercase_matching_is(temp['a'][i],n)=='f':
                temp['n'].append(n)
                temp['a'][i] = ''
    temp['a'] = [a for a in temp['a'] if a!='']

    output = dict()
    for k in temp:
        output[k] = sorted(FreqDist(temp[k]).items(),
                           key=itemgetter(1),reverse=True)
    return output
        
def text_semantics(t): # t: document-level AMR graph for text
    """ -> add 'semantics' attribute to all node in t """
    for n in t:
        if n!='0.@':
            t.node[n]['semantics'] = node_semantics(t.node[n])

def locate_uc(t,ac,uc): # ac/uc: concept in agent/user's utterance
    """ -> the most relevant node in t with the same concept c """
    temp = set() # set of all nodes with the same concept uc
    for n in t:
        if n!='0.@':
            ns = t.node[n]['semantics']
            for k in ns:
                if ns[k]!=list():
                    if k!='a':
                        if lowercase_matching_is(uc,ns[k][0][0])=='f':
                            temp.add((n,k,ns[k][0][0]))
                            break
                    else:
                        for c in [x[0] for x in ns[k]]:
                            if lowercase_matching_is(uc,c)!='n':
                                temp.add((n,k,c))
                                break
                            break
    
    #return temp
    #print(temp)
    if temp:
        # -> set of nodes in temp satifying the shortest path condition
        #tt = t.to_undirected() # simplify problem
        min_path = min([nx.shortest_path_length(t,ac,n[0])
                        for n in temp])
        min_ns = set([n for n in temp
                      if nx.shortest_path_length(t,ac,n[0])==min_path])
        return choice(list(min_ns))
    #return None
    return (None,None,uc)

def represent_concept(t,n): # t: AMR graph, n: AMR node
    """ -> most relevant concept representation (tuple) """
    ns = node_semantics(t.node[n])
    #print(n,ns)
    if 'n' in ns and ns['n']!=list():
        return (n,'n',ns['n'][0][0]) # the most relevant named entity
    elif 'a' in ns and ns['a']!=list():
        return (n,'a',ns['a'][0][0]) # the most relevant abstract concept
    return (n,'p',ns['p'][0][0]) # the most relevant pronoun
    

def initiate_concept(t,k):
    """ -> initial agent concept (tuple) """
    n = choice(top_k(t,k))[1]
    return represent_concept(t,n)

def discourse_concepts(d): # d: discourse
    """ -> set of dicourse concepts (string) """
    return set([c[2].lower() for c in d if c])    

def inside_nodes(t,d,sps): # shortest path length >2
    """ -> 'other' concept nodes inside sps """
    return set([n for sp in sps
                for n in sp[1:-1]
                if classify_node(t,n)=='other' and
                represent_concept(t,n)[2].lower() not in
                discourse_concepts(d)])
        
def neighbor_nodes(t,d,ns): # t: AMR text, ns: set of AMR nodes
    """ -> 'other' neighbor concept nodes of c1 and c2 """
    temp = set()
    for n in ns:
        temp = temp.union(set(t.neighbors(n)))
    if temp:
        temp = temp.difference(ns)
        neighbors = set([n for n in temp
                         if classify_node(t,n)=='other' and
                         represent_concept(t,n)[2].lower() not in
                         discourse_concepts(d)])
        if neighbors:
            return neighbors
        return neighbor_nodes(t,d,temp)
    return temp

def semantic_distance(t,d,n): # t: AMR text, d: discourse, n: AMR node
    """ semantic distance between n and d """
    sd = int() # semantic distance
    for i in range(len(d)-1,-1,-1):
        temp = int()
        #if d[i]:
        if d[i][0]: # d[i] corresponds to a node in AMR text
            temp = nx.shortest_path_length(t,d[i][0],n)
        sd = sd * 2 + temp
    return sd
    
def select_min_sd(t,d,ns): # t: AMR text, d: discourse, ns: AMR nodes
    """ -> set of nodes with min semantic distance """
    sds = [(n,semantic_distance(t,d,n)) # set of nodes with semantic distances
           for n in ns]
    min_sd = min(set([sd for (_,sd) in sds]))
    return choice([n for (n,sd) in sds if sd==min_sd])
    
def next_concept(t,d,k): # t: AMR text, d: discourse, k: top k
    """ -> next agent concept (tuple) """
    dd = [c for c in d if c[0]] # c: discourse concept (tuple)
    if len(dd)>=2:
        sps = nx.all_shortest_paths(t,dd[-2][0],dd[-1][0])
        if nx.shortest_path_length(t,dd[-2][0],dd[-1][0])>2:
            ins = inside_nodes(t,d,sps)
            if ins:
                return represent_concept(t,select_min_sd(t,dd,ins))
        neighbors = neighbor_nodes(t,d,[dd[-2][0],dd[-1][0]])
        if neighbors:
            return represent_concept(t,select_min_sd(t,dd,neighbors))
    elif len(dd)==1:
        neighbors = neighbor_nodes(t,d,[dd[-1][0]])
        if neighbors:
            return represent_concept(t,select_min_sd(t,dd,neighbors))
    ncs = top_k(t,k+len(dd)) # possible next concept nodes
    nc = choice([n for n in ncs #next concept node
                 if represent_concept(t,n)[2].lower()
                 not in discourse_concepts(d)]) 
    return represent_concept(t,nc)
    
def agent_concept(t,d,k): # t: AMR text, d: discourse
    """ -> agent concept (tuple) """
    if not d:
        return initiate_concept(t,k)
    return next_concept(t,d,k)

def dialog_manager(t,i,k): # t: document-level AMR graph of text
    """ for Semanland game """
    user_utterance = str()
    discourse = list()
    while (i>0):
        #print(discourse,discourse_concepts(discourse))
        ac = agent_concept(t,discourse,k) # ac: agent concept (tuple)        
        #print(nlg(ac))
        if discourse:
            print('Agent:',nlg(ac,1))
        else:
            print('Agent:',nlg(ac))
        discourse.append(ac)        
        print('#',ac)
        
        user_utterance = raw_input('User: ')
        uc = nlu(user_utterance) # uc: user concept (string)
        pc = [c for c in discourse if c[0]][-1] # previous concept        
        discourse.append(locate_uc(t,pc[0],uc))
        print('#',locate_uc(t,pc[0],uc))
            
        i -= 1
    print('Agent:',nlg(status=2))
    print(' '.join([c[2] for c in discourse]))
    discourse.append(raw_input('User: '))
    return discourse

def nlu(user_utterance): 
    """ -> concept c in user's input (simple stemming/lemmatization) """
    # http://www.nltk.org/book/ch03.html
    #c = user_utterance
    c = wnl.lemmatize(user_utterance)
    return c
    #return wnl.lemmatize(user_utterance)
    

def nlg(agent_concept=None,status=0): # 0/1/2: initial/next/final
    """ -> utterance u as agent's output """
    u = '?'
    if status==0:
        u = "Let's start with '" + agent_concept[2] +"'"
    if status==1:
        u = "Next is '" + agent_concept[2] +"'"
    if status==2:
        u = "Tell me some story related to our discourse:"
    return u
    
def main():
    """ """
    pass

if __name__ == "__main__":
##    #main()
##    amr_table = get_amr_table_path(DATA_AMR_EDITED)
##    #docids = ['Ariel','Aurora','Belle','Cinderella','Snow_White']
##    docids = ['Cinderella']
##    text = dict()
##    print('Cache size: 1')
##    tg = dict()
##    ld = dict()
##    t = dict()
##    for docid in docids:
##        print(docid)
##        text[docid] = [AMRGraph(sen=s) for _,s in sorted(amr_table[docid].items())]        
##        tg[docid],ld[docid] = define_link_concepts(text[docid],1)
##        t[docid] = merge_id_nodes(tg[docid],ld[docid])
##        #draw_graph(t[docid])
##    save_data(t['Cinderella'],'amr_cinderella.pkl')
    test = load_data('amr_cinderella.pkl')
##    dialog_manager(t['Cinderella'])
    text_semantics(test)
    tt = test.to_undirected()
    #dialog_manager(test)
    d = dialog_manager(tt,int(raw_input('i = ')),int(raw_input('k = ')))
