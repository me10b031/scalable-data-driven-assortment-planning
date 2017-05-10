# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:13:14 2017

@author: Theja
"""
import numpy as np
import time

def calcRev(ast, p, v, prod):
#v and p are expected to be n+1 and n+1 length lists respectively 
    if len(p)==prod:    
        p =  np.insert(p,0,0)   #making p a n+1 length list by inserting a 0 in the beginning
    num = 0
    den = v[0]
    for s in range(len(ast)):
        num  = num + p[ast[s]]*v[ast[s]]
        den  = den + v[ast[s]]
    rev = num/den
    return rev

def capAst_adxopt(prod, C, p, v):

    st = time.time() 
    # initialize
    b = min(C,prod-C+1) #parameter of adxopt, see Thm 3, Jagabathula 
    items = range(1,prod+1)
    removals = np.zeros(prod+1)
    set_prev = []
    rev_prev = calcRev(set_prev, p, v, prod)

    while True:
        items_left = [x for x in items if x not in set_prev]
        #Additions
        set_addition = []
        rev_addition = 0
        if len(set_prev) < C:
            for j in items_left:
                if removals[j] <b:
                    candidate_rev = calcRev(sorted(set_prev+[j]),p,v,prod)
                    if candidate_rev > rev_addition:
                        rev_addition = candidate_rev
                        set_addition = sorted(set_prev+[j])

        #Deletions
        set_deletion = []
        rev_deletion = 0
        if len(set_prev) >0:
            for idx in range(len(set_prev)):
                candidate_rev = calcRev(sorted(set_prev[:idx]+set_prev[idx+1:]),p,v,prod)
                if candidate_rev > rev_deletion:
                    rev_deletion = candidate_rev
                    set_deletion = sorted(set_prev[:idx]+set_prev[idx+1:])

        #Substitutions
        set_substitution = []
        rev_substitution = 0
        if len(set_prev) >0:
            for j in items_left:
                if removals[j] <b:
                    for idx in range(len(set_prev)):
                        candidate_rev = calcRev(sorted(set_prev[:idx]+[j]+set_prev[idx+1:]),p,v,prod)
                        if candidate_rev > rev_substitution:
                            rev_substitution = candidate_rev
                            set_substitution = sorted(set_prev[:idx]+[j]+set_prev[idx+1:])


        idx_rev_current = np.argmax(np.asarray([rev_addition,rev_deletion,rev_substitution]))
        if idx_rev_current==0:
            rev_current = rev_addition
            set_current = set_addition
        elif idx_rev_current==1:
            rev_current = rev_deletion
            set_current = set_deletion
        else:
            rev_current = rev_substitution
            set_current = set_substitution

        if rev_current <= rev_prev or np.max(removals) >= b:
            rev_current = rev_prev
            set_current = set_prev
            break
        else:
            for j in set(set_current).difference(set(set_prev)):
                removals[j] +=1

            rev_prev = rev_current
            set_prev = set_current

    timeTaken = time.time() - st  

    # print " " 
    # print "Results for oracle"
    print "Products in the adxopt assortment are", set_current 
    print "Optimal revenue is", rev_current
    # print 'Time taken for running the oracle is', timeTaken
    
    return rev_current, set_current, timeTaken
        
        