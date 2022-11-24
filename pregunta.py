"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    with open('clusters_report.txt') as txt:
        fila = txt.readlines()

    clusters = []
    cluster = [0, 0, 0, '']
    fila = fila[4:]

    for i in fila:
        
        if re.match('^ +[a-z]', i):
            principalesPalabras = i.split()
            principalesPalabras = ' '.join(principalesPalabras)
            cluster[3] = cluster[3] + ' ' + principalesPalabras

        elif re.match('^\n', i) or re.match('^ +$', i):
            cluster[3] = cluster[3].replace('.', '')
            clusters.append(cluster)
            cluster = [0, 0, 0, '']

        elif re.match('^ +[0-9]+ +', i):
            numeroCluster, cantidadPalabras, porcentajePalabras, *principalesPalabras = i.split()
            cluster[0] = int(numeroCluster)
            cluster[1] = int(cantidadPalabras)
            cluster[2] = float(porcentajePalabras.replace(',','.')) 
            principalesPalabras.pop(0) 
            principalesPalabras = ' '.join(principalesPalabras)
            cluster[3] = cluster[3] + principalesPalabras

    df = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df


# txt = open('clusters_report.txt', 'r')
# txt = txt.readlines()
# txt = txt[4:]
# ll = ''
# for line in txt:
#     ll = ll + line
# ll = ll.split('.')
# ll = ll.replace('\n', '')
# ll = ll.split('.')
# aux = []
# for linea in ll:
#     linea = linea.replace('  ', ' ')
#     linea = linea.replace('  ', ' ')
#     linea = linea.replace('  ', ' ')
#     linea = linea.replace('  ', ' ')
#     linea = linea.replace('  ', ' ')
#     aux.append([linea])

# tt = []
# print(aux[5])
# for i in aux:
#     cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave = "","","",""
#     t = i[0].rfind('%')
#     print(i[0][1:t+1].split(' '))
#     # cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave = i[0][1:t+1].split(' ')
#     principales_palabras_clave = i[0][t+1:]
#     tt.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
# print(tt)
    






    



