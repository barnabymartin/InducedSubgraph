# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:20:40 2022

@author: mpll19
"""

import networkx as nx
import itertools
from networkx.algorithms import isomorphism


### build literal gadget
list1=[['a','b'],['b','a1'],['a1','a2'],['a2','a3'],['b','b1'],['b1','b2'],['b2','b3']]
list2=[['p','q'],['q','p1'],['p1','p2'],['p2','p3'],['q','q1'],['q1','q2'],['q2','q3']]
list3=[['a1','b1'],['b1','p1'],['p1','q1'],['q1','a1']] #blue
list4=[['b','a2'],['b','b2'],['q','p2'],['q','q2'],['b1','p2'],['p1','b2']] #green
list5=[['a2','q1'],['a1','q2']] #red
list6=[['a2','q2'],['b2','p2'],['a2','q1'],['b2','p1'],['a1','q2'],['b1','p2'],['a1','b2'],['a2','b1'],['p1','q2'],['q1','p2']] #works without ['a2','b2'],['p2','q2']
list7=[['b2','p2'],['q2','a2']] #blue2 halved
list8=[['a1','b2'],['a2','b1'],['p1','q2'],['p2','q1'],['a2','b2'],['p2','q2'],['a1','q2'],['a2','q1'],['b1','p2'],['b2','p1']]
G0 = nx.Graph()
G0.add_edges_from(list1)
G0.add_edges_from(list2)
G0.add_edges_from(list3)
#G.add_edges_from(list4) not used
#G.add_edges_from(list5) not used
#G.add_edges_from(list6) not used
G0.add_edges_from(list7)
G0.add_edges_from(list8)
### end build literal gadget

### build interface gadget
list9=[[1,2],[2,3],[3,4],[5,6],[6,7],[7,8],[9,10],[11,12],[10,6],[10,2],[11,7],[11,3],[10,3],[11,2],[10,7],[11,6]]
G1 = nx.Graph()
G1.add_edges_from(list9)
### end build interface gadget

### build subgraphs 
#listH01=[[12,15],[11,12],[12,13],[14,15],[15,16]]
listH1=[[1,2],[2,3],[4,5],[5,6],[2,5]]
listH2=[[1,2],[2,3],[4,5],[5,6],[2,7],[7,5]]
listC6=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]
listC4=[[1,2],[2,3],[3,4],[4,1]]
H1 = nx.Graph()
H1.add_edges_from(listH1)
#H01 = nx.Graph()
#H01.add_edges_from(listH01)
H2 = nx.Graph()
H2.add_edges_from(listH2)
C6 = nx.Graph()
C6.add_edges_from(listC6)
C4 = nx.Graph()
C4.add_edges_from(listC4)
### end build subgraphs

#GM = isomorphism.GraphMatcher(H1,H)
#print(GM.is_isomorphic())

def subgraph_isomorphism(H,G):
    length = len(list((H.nodes())))
    iter_set = itertools.combinations(list(G.nodes),length)
    ans = False
    for x in iter_set:
        Gdash=G.subgraph(x)    
        GM = isomorphism.GraphMatcher(Gdash,H)
        if GM.is_isomorphic():
            print(x)
        ans= ans or GM.is_isomorphic()
    print(ans)

### usage, e.g.:
subgraph_isomorphism(H1,G0)
