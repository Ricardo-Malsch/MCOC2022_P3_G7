import pandas as pd
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import geopandas as gp
from shapely.geometry import Point
from datetime import datetime


tt = [datetime.now()]


def tiempo(ti=None, tf=None, generico=""):
    if ti == None:
        ti = tt[-1]
    if tf == None:
        tf = datetime.now()
        tt.append(datetime.now())
    print("tiempo{}: {:.4}s".format('' if generico == '' else ' ' + generico, (tf - ti).total_seconds()))


def uv(df, gdf_edges):
    with open("incidentes.txt", "w") as archivo:

        for index, row in df.iterrows():
            target = gp.GeoSeries(
                [
                    Point(row["Longitud"], row["Latitud"]),
                ],
                index=range(1),
                crs="EPSG:4326",
            )


            target = target.to_crs("EPSG:32719")
            #print(f'TARGET: {target}')
            distancias = gdf_edges.distance(target[0])
            distancias = distancias.sort_values()
            #print(f'DISTANCIAS: {distancias}')

            min_dist = distancias.min()
            #print(f'MIN_ DIST: {min_dist}')
            indice_min = distancias.idxmin()
            #print(f'INDICE MIN: {indice_min}')
            lista = distancias.to_frame()
            lista_calles = []
            for i, rower in lista.iterrows():
                u, v, k = i
                try:
                    nombre_calle = G.edges[u, v, k]["name"]
                    if nombre_calle not in lista_calles:
                        lista_calles.append(nombre_calle)
                    #print(f'NOMBRE 1: {nombre_calle}')
                except:
                    continue
                #print(i, row)

                if len(lista_calles) == 2:
                    break
            fecha = parsefecha(row["Tiempogps"])
            lista_calles.append(fecha)
            lista_calles.append(row['Velocidad'])
            if float(row['Velocidad']) <= 10.0:
                archivo.write(f'{fecha} {lista_calles[0]} - {lista_calles[1]} {lista_calles[3]}km/h\n')

            u, v, k = indice_min
            df.at[index, "u,v"] = f"{u},{v},{k}"
            if index == 200000:
                return df

    return df

def parsefecha(fecha):
    fecha = str(fecha)
    i = f"{fecha[:8]} {fecha[8:10]}:{fecha[10:12]}"
    #t = datetime.strptime(i, '%H:%M')
    return i

def parsefechaDate(fecha):
    fecha = str(fecha)
    i = f"{fecha[8:10]}:{fecha[10:12]}"
    t = datetime.strptime(i, '%H:%M')
    return t

def tiempoG(df):
    tiempo_inicial = parsefechaDate(df.loc[0]['Tiempogps'])
    lista_general = []
    dicc = {}
    titles = []
    m = 0
    for index, row in df.iterrows():

        tiempo_row = parsefechaDate(row['Tiempogps'])
        diff = (tiempo_row - tiempo_inicial).total_seconds()


        if index == 200000:
            string_time = parsefecha(row['Tiempogps'])
            titles.append(string_time)
            lista_general.append(dicc)
            return lista_general, titles
        if diff <= 300:

            if row['u,v'] not in dicc:
                #print(index)
                # title = i
                dicc[row['u,v']] = {'cant': 1, 'vel': row['Velocidad']}
            else:
                print(index)
                dicc[row['u,v']]['cant'] += 1
                dicc[row['u,v']]['vel'] += row['Velocidad']
            # print(diff)
        else:
            string_time = parsefecha(row['Tiempogps'])
            titles.append(string_time)
            lista_general.append(dicc)

            dicc = {}
            dicc[row['u,v']] = {'cant': 1, 'vel': row['Velocidad']}
            tiempo_inicial = parsefechaDate(row['Tiempogps'])
    print("------------")
    print(len(lista_general))
    print("-------------")
    tiempo()
    return lista_general, titles


def grafico(lista, G, titles):
    indx = 52
    ind = 1
    for dicc_min in lista:
        ax = plt.subplot(111)
        ax.axis("off")
        # print(ax)
        gdf_edges.plot(ax=ax, color="#848484")
        for key in dicc_min.keys():
            aux = key.split(",")
            u, v, k = int(aux[0]), int(aux[1]), int(aux[2])
            # print(u,v)

            xi = G.nodes[u]["x"]
            yi = G.nodes[u]["y"]
            xj = G.nodes[v]["x"]
            yj = G.nodes[v]["y"]

            # print(xi,xj,yi,yj)
            vel = dicc_min[key]['vel'] / dicc_min[key]['cant']

            try:
                nombre_calle = G.edges[u, v, k]["name"]

                # print(nombre_calle)
                if vel < 10:
                    gdf_edges[gdf_edges.name == nombre_calle].plot(ax=ax, color="red")
                elif vel >= 10 and vel <= 18:

                    gdf_edges[gdf_edges.name == nombre_calle].plot(ax=ax, color="yellow")
                elif vel > 19 and vel <= 36:

                    gdf_edges[gdf_edges.name == nombre_calle].plot(ax=ax, color="blue")
                else:
                    gdf_edges[gdf_edges.name == nombre_calle].plot(ax=ax, color="green")

            except:
                continue

                # print("GRAFICOOOOOOOOOO")
        plt.title(titles[ind-1])
        plt.savefig(f"images/pag{indx}.png")
        indx+=1
        ind += 1
        # plt.show()


def graficoIncidentes(lista, G, titles):
    indx = 52
    ind = 1
    for dicc_min in lista:
        ax = plt.subplot(111)
        ax.axis("off")
        # print(ax)
        gdf_edges.plot(ax=ax, color="#848484")
        for key in dicc_min.keys():
            aux = key.split(",")
            u, v, k = int(aux[0]), int(aux[1]), int(aux[2])
            # print(u,v)

            xi = G.nodes[u]["x"]
            yi = G.nodes[u]["y"]
            xj = G.nodes[v]["x"]
            yj = G.nodes[v]["y"]

            # print(xi,xj,yi,yj)
            vel = dicc_min[key]['vel'] / dicc_min[key]['cant']

            try:
                nombre_calle = G.edges[u, v, k]["name"]

                # print(nombre_calle)
                if vel < 3:
                    gdf_edges[gdf_edges.name == nombre_calle].plot(ax=ax, color="red")

            except:
                continue


        plt.title(titles[ind-1])
        plt.savefig(f"incidentesImages/pag{indx}.png")
        indx+=1
        ind += 1
        # plt.show()



ox.settings.log_console = False
ox.settings.use_cache = True

G = ox.graph_from_bbox(
    north=-33.3753,
    south=-33.4108,
    east=-70.6030,
    west=-70.5417,
    network_type="drive",
    clean_periphery=True, )

print("---------------------")
print("---------------------")
print("---------------------")

from pyproj import CRS

crs = CRS.from_proj4("+proj=utm + zone=19 + south +datum=WGS84 + units= km + no_defs")
utm = "EPSG:32719"
utm = crs
# for e in G.edges:
#     ni,nj,k=e
#     edgeinfo=G.edges[ni,nj,k]
#     #print(f"ni={ni} nj={nj} k={k}")
#     print(f"edgeinfo={edgeinfo}")


gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
gdf_edges = gdf_edges.to_crs("EPSG:32719")
gdf_nodes = gdf_nodes.to_crs("EPSG:32719")

archivo = 'Detalle_nuevo2_Registros_GPS_20170912.csv'

df = pd.read_csv(archivo, header=0, encoding="latin_1", sep=";",
                 usecols=["Latitud", "Longitud", "Tiempogps", "Velocidad"])

df = uv(df, gdf_edges)
#print(df)
#print("U,v")
li = tiempoG(df)
lista_calles = li[0]
titles = li[1]
#print(li)
#print("clasifica")

grafico(lista_calles, G, titles)
graficoIncidentes(lista_calles, G, titles)