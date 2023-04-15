from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt
import nltk
import math
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
#node={}
pnode={}
#qry=raw_input("Enter Query ->")

qry="boy has more red balls than blue balls"

qrywd=nltk.word_tokenize(qry)
#print qrywd
tag=nltk.pos_tag(qrywd)
#print tag

G=nx.DiGraph()
fname=qry+str('.txt')
#DD=nx.DiGraph()
x1=1.0
y1=0.8
m1=0.6
l1=0.4
xnode={}


def getRelation(wd,sy):
  #hypo = lambda s: s.hyponyms()
  hx=sy.hypernyms()
 # hx=hx+ sy.root_hypernyms()
  hy=sy.hyponyms()
  #hy=sy.closure(hypo, depth=)
  mx=sy.member_meronyms()
  #mx=mx+sy.part_meronyms()
  hl=sy.part_holonyms()
 # hl=hl + sy.member_holonyms()
  
  ''' 
  lm=sy.lemmas()
  for l in lm:
    t=l.derivationally_related_forms()
    for f in t:
     ss=f.synset()
     if G.has_node(str(ss))== False:
       G.add_node(str(ss)) 
     G.add_edge(str(ss),str(sy),weight=1)
     G.add_edge(str(sy),str(ss),weight=1)
    '''   
 
  for i in hx:
   #print i
   if str(i) not in pnode: 
    pnode.update({str(i):1})
    #node.update({str(i):1})
    G.add_node(str(i))
 #  xx[v]=str(i)
 #  v=v+1
 #  pos.extend(xx)
   G.add_edge(str(sy),str(i),weight=x1)
   G.add_edge(str(i),str(sy),weight=x1)
   
  for i in hy:
   if str(i) not in pnode: 
    pnode.update({str(i):1})
    #node.update({str(i):1})
    G.add_node(str(i))
 #  xx[v]=str(i)
 #  v=v+1
 #  pos.extend(xx)
   G.add_edge(str(sy),str(i),weight=y1)
   G.add_edge(str(i),str(sy),weight=y1)

  for i in mx:
   if str(i) not in pnode: 
    pnode.update({str(i):1})
    #node.update({str(i):1})
    G.add_node(str(i))
 #  xx[v]=str(i)
 #  v=v+1
 #  pos.extend(xx)
   G.add_edge(str(sy),str(i),weight=m1)
   G.add_edge(str(i),str(sy),weight=m1)
  

  for i in hl:
   if str(i) not in pnode: 
    pnode.update({str(i):1})
    #node.update({str(i):1})
    G.add_node(str(i))
 #  xx[v]=str(i)
 #  v=v+1
 #  pos.extend(xx)
   G.add_edge(str(sy),str(i),weight=l1)
   G.add_edge(str(i),str(sy),weight=l1)  
   

fn=[]
x=0
for wd in tag: 
 if((wd[1])[0].lower()=='v' or (wd[1])[0].lower()=='n' or (wd[1])[0].lower()=='j'):
  x=x+1
 # G.add_node(str(wd))
  pnode.update({str(wd):2}) 
  #node.update({str(wd):1})
  syn=wn.synsets(wd[0])
 # syn.reverse();
  #print syn
 # for sn in syn:
#    fn.append(str(sn))
 #  G.add_node(str(sn))
  # G.add_edge(str(sn),str(wd),weight=1)
   #G.add_edge(str(wd),str(sn),weight=1) 
  p=str(wd)
  #print node
  #pos[wd]=1 
  for sy in syn:
   # print "hero"
    
 
    if str(sy) not in pnode:
      pnode.update({str(wd):1}) 
   #   node.update({str(wd):1})
      getRelation(wd,sy)
      pnode[str(sy)]=2 
    G.add_edge(str(wd),str(sy),weight=1)
    G.add_edge(str(sy),str(wd),weight=1)
    pnode[str(wd)]=2
 else:
  x=x+1








d=0
while(d<4):
   xnode.update(pnode)
#   print 'ggg'
   for i in xnode:
    if xnode[str(i)]!=2:
      syn=wn.synsets(str(i.split('.', 1 )[0][8::]))
      
      xnode[str(i)]=2
     # print syn
      for sy in syn:
       if sy not in pnode:
        
        getRelation(i,sy)
        pnode.update({str(sy):2})
    #    node.update({str(sy):1})
        
      #print i.split('.', 1 ) 
      #print i.split('.', 1 )[0][8::]
      d=d+1;
      

#print 'xxxxx'
#print G.has_node(str( Synset('drinking.n.01')))
#print 'pppappu'
print (G.number_of_nodes())

#fn=[]
for j in tag:
 if((j[1])[0].lower()=='v' or (j[1])[0].lower()=='n' or (j[1])[0].lower()=='j'):
  for i in tag: 
   if((i[1])[0].lower()=='v' or (i[1])[0].lower()=='n' or (i[1])[0].lower()=='j'):
    if str(i)!= str(j):
     for path in nx.all_simple_paths(G,source=str(i),target=str(j)):
     # print path
      #print 'ttt'
      
      for i in path:
       if i not in fn:
        
        fn.append(str(i))
   
   #  for path in nx.all_simple_paths(G,source=str(i),target=str(j)):
    #  for i in path:
     #  if i not in fn:
      #  fn.append(str(i))
        

'''
fn=[]
for j in tag:
  if((j[1])[0].lower()=='v' or (j[1])[0].lower()=='n'):
    fn.append(str(j))
    for i in pnode:
     if G.has_node(str(i)):
      if nx.has_path(G,str(j),str(i)):
       fn.append(str(i))
   '''   
#print (len(fn)) 
#print pnode
s= G.subgraph(fn)
#print s.number_of_nodes()
#print ""
"""
for st in fn:
 print st
 if (st != "('milk', 'NN')") or (st != "('drink', 'VBZ')"):
  n=len(st)
  #st[8:n-2:]
  sy=wn.synset(str(st[8:n-2:]))

  lm=sy.lemmas()
 # print "hhhh"
  for l in lm:
    t=l.derivationally_related_forms()
    for f in t:
     ss=f.synset()
     if G.has_node(str(ss))== False:
       G.add_node(str(ss)) 
     G.add_edge(str(ss),str(sy),weight=1)
     G.add_edge(str(sy),str(ss),weight=1)

"""
##compactness
sum=0.0;
for u in fn:
 for v in fn:
  if (u != v):
   sum=sum+ nx.shortest_path_length(s, source=str(u), target=str(v), weight='weight')
   
v=s.number_of_nodes()
max=2*v*v*(v-1)
min=v*(v-1)
compt=(max-sum)/(max-min)

print (str(1+4))

fo = open("test.txt", "w+")
fo.write('hypernym='+str(x1)+'\nhyponyms='+str(y1)+'\nmeronyms='+str(m1)+'\nholonyms='+str(l1))
fo.write('\n\ntaged word='+str(tag))  
fo.write('\n\nnumber of nodes in graph='+str(v))
print("Number of nodes:",v)
fo.write('\n\nCompactness='+str(compt))
print("Compactness:",compt)
#fo.write("\n\nCompactness=")



#print len(pnode)


entropy=0;
for i in fn:
  deg=s.degree(str(i),weight='weight')
  deg1=2*s.number_of_edges()
  p_v=deg/float(2*s.number_of_edges())
  #p_v=deg/float(deg1)
  #f=math.log(p_v)
  entropy=entropy + (p_v*(math.log(p_v)))*(-1)
entropy=entropy/math.log(len(fn),2)

#print "entrop="+str(entropy)
fo.write('\n\nentropy='+str(entropy))
print("Entropy:",entropy)
density=nx.density(s)

#print "density="+str(density)
fo.write("\n\ndensity="+str(density))
print("Edge density:",density)
f_numerator = ((3*entropy)+(2*density)+compt)
f_final = f_numerator/3
print("F:",f_final)

degree_centrality=nx.degree_centrality(s)

#print "degree_centrality="+str(degree_centrality)
fo.write("\n\ndegree_centrality="+str(degree_centrality))
print("Degree_centrality:",degree_centrality)
betweenness_centrality=nx.betweenness_centrality(s, k=None, normalized=True, weight='weight', endpoints=False, seed=None)

#print "betweenness_centrality="+str(betweenness_centrality)
fo.write("\n\nbetweenness_centrality="+str(betweenness_centrality))
print("Betweeness:",betweenness_centrality)
#eigenvector_centrality=nx.eigenvector_centrality(s, max_iter=1000, tol=1e-06, nstart=None)
#print eigenvector_centrality
closeness_centrality=nx.closeness_centrality(s, u=None, distance='weight', wf_improved=True)
#print "closeness_centrality="+str(closeness_centrality)
fo.write("\n\ncloseness_centrality="+str(closeness_centrality))
print("Closeness:",closeness_centrality)
pagerank=nx.pagerank(s, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)  
#print nx.pagerank(s)
#print "pagerank="+str(pagerank)
fo.write("\n\npagerank="+str(pagerank))
print("Pagerank:",pagerank)


#hubs,authorities=nx.hits(s, max_iter=1000, tol=1e-08, nstart=None, normalized=True)
#print "hubs="+str(hubs)
#print ""
#print "authorities="+str(authorities)
fo.close()


print (len(pnode))
#nx.draw_networkx(s, pos=mapp, with_labels=True) 
f=nx.convert_node_labels_to_integers(s, 0, ordering='default', label_attribute='ggg')

nx.draw(s,with_labels=True)
cde=str(qry)+str('.png')
plt.savefig('F:/PRAKHAR/Machine Learning/SENTIMENT ANALYSIS/'+cde) 
plt.show()

