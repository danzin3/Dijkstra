
import graph

import best_way

#Criando-se um grafo com 8 vértices e o valor 0 como padrão da matriz de Adjacentes:
objGrafo = graph.Graph(8,0)

#Inserindo arestas de forma que em que...
#param1 = vértice1, param2 = vértice2, param3 = valor do peso (aresta) entre os dois vértices
objGrafo.setWeight(0,1,6);objGrafo.setWeight(0,2,5)
objGrafo.setWeight(1,2,4);objGrafo.setWeight(1,3,6)
objGrafo.setWeight(2,6,3);objGrafo.setWeight(2,5,2)
objGrafo.setWeight(2,4,3);objGrafo.setWeight(2,3,7)
objGrafo.setWeight(3,4,6);objGrafo.setWeight(3,7,4)
objGrafo.setWeight(4,7,2);objGrafo.setWeight(4,5,4)
objGrafo.setWeight(5,6,8)

#Criando-se um objeto para conter os dados do melhor caminho onde...
#param1 = quant vertices do grafo, param2 = vértice de Origem, param3= vertice de Destino
objWay = best_way.Way(8,1,7)

# Algoritmo:

while(objWay.hasAllChecked() == False):
    
    minVertice = objWay.getMinItem() # Pega o vértice de menor distância do vetor caminho
    
    if(objGrafo.hasAdj(minVertice)): # Tem adjacentes ?
        
        listaAdj = objGrafo.getListAdj(minVertice) # Pega Todos os Adjacentes de minVertice

        # Percorre a lista de adjacentes do minVertice:
        for line in listaAdj:
            # Pega o peso entre minVertice e line:
            wightEdge = objGrafo.getWeight(minVertice,line)

            if(objWay.item[line].distancia > (objWay.item[minVertice].distancia + wightEdge)):
                objWay.item[line].distancia = objWay.item[minVertice].distancia + wightEdge
                objWay.item[line].antecessor = minVertice
    
    # Marca esse vértice para não passar nele de novo
    objWay.item[minVertice].marca = True

# Obtém os vértices finais que correspondem ao menor caminho entre 1 e 7 no exemplo
result = objWay.getListFinal()

for line in result:
    print(line)