# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:06:56 2016

@author: Deeksha
"""

import numpy
   
 #match answers with the test API
   #dataset = genDataSet(p, K, prod, C)
   #queryset = numpy.reshape(v[1:], (1, prod))
   #test_approxNN('mips', dataset, queryset, R_lsh, p_lsh)
   
    

#parameters required
prod = 100 #number of products
C=3    #capacity of assortment
price_range = 2; #denotes highest possible price of a product
eps = 0.25 #tolerance
R_lsh =8 # R parameter for the simple LSh algorithm
p_lsh = 0.9 # success probability parameter for the simple LSH algorithm

#generating the price and customer preference vector
p = numpy.random.uniform(0,price_range, prod) # create an array of n+1 uniform random numbers between 0 and price_range  
p = numpy.around(p, decimals =2)
p =  numpy.insert(p,0,0) #inserting 0 as the first element to denote the price of the no purchase option
v = numpy.random.rand(prod+1) #v is a prod+1 length vector as the first element signifies the customer preference for the no purchase option
 
#calling the new algorithm to find optimal assortment                 
capAst_LSH(prod, C, p, v, eps, R_lsh, p_lsh)

#finding the optimal assortment using Paat's algorithm
capAst_paat(prod, C, p, v)

#finding the optimal assortment by exhaustive search to compare results
capAst_oracle(prod, C, p, v)


#prod = 4
#C =2
#p = numpy.asarray([0,9.5, 9, 7, 4.5])
#v = numpy.asarray([1, 0.2, 0.6, 0.3, 5.2])