#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
cosi299a - Cinderella
alexluu@brandeis.edu
"""
import os

PROJECT = os.getcwd()
DATA = os.path.join(PROJECT, 'Data')
DATA_AMR = os.path.join(DATA, 'amr')
DATA_AMR_EDITED = os.path.join(DATA, 'amr_edited')
DATA_AMR_LPP = os.path.join(DATA, 'amr_lpp')
DATA_AMR_LPP_01 = os.path.join(DATA_AMR_LPP, '01')
DATA_AMR_LPP_02 = os.path.join(DATA_AMR_LPP, '02')
DATA_AMR_ANNOTATED = os.path.join(DATA, 'amr_annotated')
DATA_AMR_ANNOTATED_LPP_01 = os.path.join(DATA_AMR_ANNOTATED, 'amr_lpp_01.xml')
DATA_AMR_ANNOTATED_LPP_02 = os.path.join(DATA_AMR_ANNOTATED, 'amr_lpp_02.xml')

# maybe dict instead of set???
AMR_SPECIAL_CONCEPTS = { # excluding named entity related concepts
    # wh-words in wh-questions
    'amr-unknown',
    #amr-unintelligible,
    # ordinals
    'ordinal-entity',
    # absolute time
    'date-entity', 'date-interval',
    # relative time
    'monetary-quantity', 'distance-quantity', 'area-quantity',
    'volume-quantity', 'temporal-quantity', 'frequency-quantity',
    'speed-quantity', 'acceleration-quantity', 'mass-quantity',
    'force-quantity', 'pressure-quantity', 'energy-quantity',
    'power-quantity', 'voltage-quantity', 'charge-quantity',
    'potential-quantity', 'resistance-quantity', 'inductance-quantity',
    'magnetic-field-quantity', 'magnetic-flux-quantity',
    'radiation-quantity', 'concentration-quantity', 'temperature-quantity',
    'score-quantity', 'fuel-consumption-quantity', 'seismic-quantity',
    # mathematical operators
    'product-of', 'sum-of',
    # percentage
    'percentage-entity',
    # phone number
    'phone-number-entity',
    # email address
    'email-address-entity',
    # url
    'url-entity',
    }

NOMINATIVE_PRONOUNS = {
    'i', 'we',
    'you', "y'all",
    'he', 'she', 'it', 'they',
    'one',
    }
AMR_CONJUNCTIONS = {
    'and', 'or', 'either', 'neither',
    #'contrast-01',
    }

PREDICATE_NOUNS = { # followed by inverse core role events
    'thing', 'organization', 'person'
    }

DEIXIS = {
    'this','that','here','there'
    }
