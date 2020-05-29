''' 
Objeto que possúi a lista de melhor caminho assim como os métodos necessários...
para a implementação do algoritmo de Dijkstra

É bom saber que os vértices do grafo devem ser enumerados, para se trabalhar com eles

A classe Way possúi uma lista de itens, onde cada item possui os atributos descritos...
na classe Item... O peso das arestas podem ser mais complexos como valores decimais
'''
from math import inf # Valor infinto em python

class Item:
    def __init__(self):
        self.antecessor = 0 # Inteiro para representar outro vértice
        self.distancia = 0  # Inteiro, para representar a distância (peso) entre dois vértices
        self.marca = False   # Booleano


class Way:
    # O parametro n é a quantidade de vértices do grafo
    def __init__(self,n,vOrigem,vDestino):
        self.numItens = n
        self.item = []
        self.origem = vOrigem
        self.destino = vDestino

        for i in range(n):
            # Instancia um objeto do tipo Item e insere ele na lista item que ta dentro de Way
            aux = Item()
            aux.antecessor = -1
            aux.distancia = inf
            aux.marca = False
            self.item.append(aux)
        # A distância da origem é sempre a menor possível, então:
        self.item[vOrigem].distancia = 0
    
    # Método Booleano para verificar se todos os vértices já foram visitados
    def hasAllChecked(self):
        # True --> Vértice Visitado; False --> Vértice ainda não visitado
        try:
            for i in self.item:
                if(i.marca == False):
                    return False
            return True
        except Exception as e:
            print("Erro ao executar o procedimento\nMotivo: ",e)
    
    # Método para retornar o índice do primero menor item ainda não visitado da lista de Melhor Caminho
    def getMinItem(self):
        try:
            minDistance = inf
            minItem = 0
            c = 0
            while(c < self.numItens):
                if(self.item[c].marca == False):
                    if(self.item[c].distancia < minDistance):
                        minDistance = self.item[c].distancia
                        minItem = c
                c = c + 1
            return minItem
        except Exception as e:
            print("Erro ao executar o procedimento\nMotivo: ",e)
    
    # Método que retorna a lista de vértice que corresponde o menor caminho:
    def getListFinal(self):
        if(self.hasAllChecked() == True):
            try:
                resp = []
                dest = self.destino
                while(dest != self.origem):
                    resp.append(dest)
                    dest = self.item[dest].antecessor
                resp.append(dest)
                return resp
            except Exception as e:
                print("Não foi possível realizar econtrar o caminho\nMotivo: ",e)
                return None
        else:
            print("O melhor caminho ainda não está pronto\nAinda existem vértices não visitados")
            return None
     # Método para zerar os campos do objeto, caso for necessário utilizá-lo novamente mais de uma vez
    """
    def clearAll(self):
        try:
            self.numItens = None
            self.item.clear()
            self.origem = None
            self.destino = None
            print("Objeto Esvaziado com sucesso!")
        except Exception as e:
            print("Não foi possível esvaziar o objeto.\nMotivo: ",e)
    """