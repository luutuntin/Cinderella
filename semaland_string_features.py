#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, with_statement


"""
cosi299a- Cinderella
alexluu@brandeis.edu
"""

def truecase_is(string):
    """ -> lower/title/upper/other """
    if string.islower():
        return 'l'
    if string.istitle():
        return 't'
    if string.isupper():
        return 'u'
    return 'o'

def alnum_is(string):
    """ -> alpha/digit/other """ #assumption: only alnum strings analyzed
    if string.isalpha():
        return 'a'
    if string.isdigit():
        return 'd'
    return 'o'

def truecase_matching_is(str1, str2):
    """ -> f(ull-string)/s(ub-string)/n(one) """
    if str1==str2:
        return 'f'
    if str1 in str2:
        return 's'
    return 'n'

def lowercase_matching_is(str1, str2):
    return truecase_matching_is(str1.lower(),str2.lower())
