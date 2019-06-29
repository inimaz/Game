# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:18:50 2019

@author: iimazchacon
"""

#This file is to initialize all the globals
import numpy as np
import core as c
def initialize(n_players):
    
    global n_countries
    global year
    global conq_countries
    global world
    global size_world
    
    n_countries= n_players**2
    year = 0
    conq_countries = np.zeros((n_players,1))
    world = np.zeros((n_players,n_players))-1
    size_world = np.shape(world)[1]