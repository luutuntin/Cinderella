#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, with_statement


"""
cosi299a- Cinderella
alexluu@brandeis.edu
"""

from nltk.corpus import wordnet as wn
from nltk.corpus import names


# lists of male and female first names - NLTK
m = set(names.words('male.txt'))
f = set(names.words('female.txt'))
mm = m.difference(f).union({'he','Mr.'})
ff = f.difference(m).union({'she','Ms.','Mrs.'})

# http://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html
#{ Part-of-speech constants
ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
#}

POS_LIST = [NOUN, VERB, ADJ, ADV]
POS_SET = {'a','r','n','v'}

def synonyms(word,pos=POS_SET):
    """ -> WordNet synonyms of a word """
    return set(l for s in wn.synsets(word)
                 if s.pos() in pos
                 for l in s.lemma_names())

def hypernyms(word,pos=POS_SET):
    """ -> WordNet hypernyms of a word """
    return set(l for s in wn.synsets(word)
                 if s.pos() in pos
                 for p in s.hypernym_paths()
                 for h in p
                 for l in h.lemma_names())

# reference:
# sujitpal.blogspot.com/2014/12/semantic-similarity-for-short-sentences.html
#def get_best_synset_pair(word_1, word_2):
def get_best_synset_pair(word_1,word_2,pos_1=POS_SET,pos_2=POS_SET):
    """ 
    Choose the pair with highest path similarity among all pairs. 
    Mimics pattern-seeking behavior of humans.
    """    
    #synsets_1 = wn.synsets(word_1)
    synsets_1 = [s for s in wn.synsets(word_1) if s.pos() in pos_1]
    #synsets_2 = wn.synsets(word_2)
    synsets_2 = [s for s in wn.synsets(word_2) if s.pos() in pos_2]    
    max_sim = None
    best_pair = None, None
    for synset_1 in synsets_1:
        for synset_2 in synsets_2:
            if synset_1.pos()==synset_2.pos():
                #sim = wn.path_similarity(synset_1, synset_2)
                sim = wn.lch_similarity(synset_1, synset_2) # same POS needed
                if (max_sim==None) or (max_sim<sim):
                    max_sim = sim
                    best_pair = synset_1, synset_2
    #if best_pair!=(None,None): # or max_sim!=None
    if max_sim!=None:
        spd = best_pair[0].shortest_path_distance(best_pair[1])
        lch = best_pair[0].lowest_common_hypernyms(best_pair[1])
        lch_depth = None
        if lch:
            lch_depth = max(s.min_depth() for s in lch)
        return best_pair, max_sim, spd, lch_depth
    return None


def gender(word):
    """ -> m(ale)/f(emale)/u(nknown) """
    if (word in mm) or \
       (('male' in hypernyms(word)) and\
        ('female' not in hypernyms(word))):
        return 'm'
    if (word in ff) or \
       (('female' in hypernyms(word)) and\
        ('male' not in hypernyms(word))):
        return 'f'
    return 'u'

##def gender_constraint(w1,w2):
##    """ passed/failed """
##    if (gender(w1)=='m' and gender(w2)=='f') or \
##       (gender(w1)=='f' and gender(w2)=='m'):
##        return 'failed'
##    return 'passed'

def gender_constraint(w1,w2):
    """ passed/failed """
    if gender(w1)==gender(w2):
        return 'passed'
    return 'failed'

def gender_constraint_pro(p,w): # p: pronoun, w: word
    """ passed/failed """
    if (gender(p)=='m' and gender(w)=='f') or \
       (gender(p)=='f' and gender(w)=='m'):
        return 'failed'
    return 'passed'

##def animacy(word):
##    """ -> person(.n.01)/animal(.n.01)/other """
##    output = set()
##    if (word in {'i','we','you',"y'all",'he','she'}) or \
##       (('person' in hypernyms(word) and \
##        ('animal' not in hypernyms(word)))):       
##        return 'p'
##    if 'animal' in hypernyms(word):
##        return 'a'
##    return 'o'

def animacy(word):
    """ -> person(.n.01)/animal(.n.01)/other """
    output = set()
    if (word in {'i','we','you',"y'all",'he','she'}) or \
       ('person' in hypernyms(word)):
        output.add('p')
    if 'animal' in hypernyms(word):
        output.add('a')
    return output
    
def animacy_constraint(w1,w2):
    """ passed/failed """
    if animacy(w1)==animacy(w2):
        return 'passed'
    return 'failed'

def animacy_constraint_pro(p,w): # p: pronoun, w: word
    """ passed/failed """
    if ('p' in animacy(p)) and ('p' not in animacy(w)):
        return 'failed'
    return 'passed'
