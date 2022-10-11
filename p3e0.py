# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:51:01 2022

@author: camm2
"""

import networkx as nx 
import osmnx as ox 
import matplotlib.pyplot as plt 
from matplotlib.pylab import *


gtfs={}

fname="shapes.txt"

#with open(fname,"r") as fid:
    #for line_number, line in enumerate(fid):
        #if line_number >0:
            #recorrido,lat,lon,corr=line.split(sep=",")
            #lat=double(lat)
            #lon=double(lon)
            #corr=int32(corr)
            #if not recorrido in gtfs:
                #gtfs[recorrido]=[[lat],[lon],[corr]]
            #else:
                #gtfs[recorrido][0].append(lat)
                #gtfs[recorrido][1].append(lon)
                #gtfs[recorrido][2].append(corr)
                
           # gtfs[recorrido]
#iniciales=["101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","125","126","2","3","4","5","6","7","B","C","D","E","F","G","H","I","J"]   
#colores=["#FBFF00","#FBFF00","#FF9B00","#FBFF00","#FF0400","#FF9B00","#FF9B00","#FBFF00","#38C8B0","#38C8B0","#23700A","#2015A5","#23700A","#FBFF00","#38C8B0","#FF0400","#FF9B00","#38C8B0","#23700A","#FF0400","#23700A","#23700A","#23700A","#2015A5","#23700A","#FF9B00","#38C8B0","#FF0400","#FBFF00","#FF0400","#FF0400","#FF9B00","#23700A","#FBFF00","#2015A5","#23700A","#23700A","#38C8B0"]        
#          101       102        103       104       105      106        107       108       109      110        111      112        113      114       115        116       117       118       119      120      121       125        126        2         3        4          5         6           7       B          C         D         E          F        G          H         I       J

#for l in range(len(iniciales)): 
    
  #  for key in gtfs.keys():
       # lat, lon, corr =gtfs[key]
        
        #if key[0]==iniciales[l]:
           # plot(lon, lat, color=colores[l])    
   # print(l)           
            
#for key in gtfs.keys():
    #lat, lon, corr =gtfs[key]
    #plot(lon, lat)
    
    
#    
#       print(key)
            

#axis("equal")
#show()

ox.settings.log_console=True
ox.settings.use_cache=True

G= ox.graph_from_bbox(
north=-33.3505,
south=-33.5993,
east=-70.4910,
west=-70.8429,
network_type="drive",
clean_periphery=True,
#custom_filter='["highway"~"tertiary|secondary"]'
    
    )

print("------------")
print("------------")
print("------------")
#print(G.edges)

#for n in G.nodes:
   #print(n)
   #print(G.nodes[n])
    
for e in G.edges:
   ni,nj,k=e 
   edgeinfo=G.edges[ni,nj,k]
   #print(f"ni={ni} nj={nj} k={k}")
   #print(f"edgeinfo={edgeinfo}")

#plt.figure()
ax=plt.subplot(111)

pos={}
for nodo in G.nodes:
    pos[nodo]=(G.nodes[nodo]["x"], G.nodes[nodo]["y"])
    



#labels={}

#nx.draw_networkx_nodes(G, pos,node_size=1, node_color='black')
#nx.draw_networkx_edges(G,pos=pos)
#nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=labels)   
count=0
lista=[]
lista2=[]
for ni,nj, k in G.edges:
    #print(G.edges[ni,nj,k])
    highway=G.edges[ni,nj,k]["highway"]
    xi=G.nodes[ni]["x"]
    yi=G.nodes[ni]["y"]
    xj=G.nodes[nj]["x"]
    yj=G.nodes[nj]["y"]
    #if highway == "primary":
       
       
    
       
    
    if "name" in G.edges[ni,nj,k]:
        nombre=G.edges[ni,nj,k]["name"]
       
    
        #x0=(xi+xj)/2
       # y0=(yi+yj)/2
        #print(f"Incluyendo calle {nombre} en x0={x0} y0={y0}")
 
        
        if nombre in lista:
            pass
        else:
            lista.append(nombre)
            #lista2.append(highway)
            #ax.text(x0,y0,s=nombre,fontsize=4)
    
    #if 
        #ax.text(x0,y0,s=nombre)
     #ax.plot(x0,y0,".")
        #ax.annotate(nombre,(y0,x0))
        if highway == "motorway":
            i=(xi,xj)
            j=(yi,yj)
            plt.plot(i,j, color="yellow")
        if highway == "primary":
            c=(xi,xj)
            v=(yi,yj)
            plt.plot(c,v, color="grey")
        if highway == "secondary":
            r=(xi,xj)
            p=(yi,yj)
            plt.plot(r,p, color="grey")
            
with open(fname,"r") as fid:
    for line_number, line in enumerate(fid):
        if line_number >0:
            recorrido,lat,lon,corr=line.split(sep=",")
            lat=double(lat)
            lon=double(lon)
            corr=int32(corr)
            if not recorrido in gtfs:
                gtfs[recorrido]=[[lat],[lon],[corr]]
            else:
                gtfs[recorrido][0].append(lat)
                gtfs[recorrido][1].append(lon)
                gtfs[recorrido][2].append(corr)
                
            gtfs[recorrido]
iniciales=["101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","125","126","2","3","4","5","6","7","B","C","D","E","F","G","H","I","J"]   
colores=["#FBFF00","#FBFF00","#FF9B00","#FBFF00","#FF0400","#FF9B00","#FF9B00","#FBFF00","#38C8B0","#38C8B0","#23700A","#2015A5","#23700A","#FBFF00","#38C8B0","#FF0400","#FF9B00","#38C8B0","#23700A","#FF0400","#23700A","#23700A","#23700A","#2015A5","#23700A","#FF9B00","#38C8B0","#FF0400","#FBFF00","#FF0400","#FF0400","#FF9B00","#23700A","#FBFF00","#2015A5","#23700A","#23700A","#38C8B0"]        
#          101       102        103       104       105      106        107       108       109      110        111      112        113      114       115        116       117       118       119      120      121       125        126        2         3        4          5         6           7       B          C         D         E          F        G          H         I       J

for l in range(len(iniciales)): 
    
    for key in gtfs.keys():
        lat, lon, corr =gtfs[key]
        
        if key[0]==iniciales[l]:
            plot(lon, lat, color=colores[l])    
            
        
        
     #count+=1
#gdf_nodes,gdf_edges =ox.graph_to_gdfs(G)
#gdf_edges[gdf_edges.highway =="motorway"].plot(ax=ax, color="#848484")
#gdf_nodes.plot(ax=ax)
nx.write_gpickle(G, 'grafo_santiago_grupo07.gpickle')

#print(lista2)
plt.axis("equal")
plt.show()
plt.savefig("mapagrupo07.png")
