# Classe para a criação e manipulação de um grafo e suas funções mais comuns

class Graph:

    # Onde n é a quantidade de vértices do grafo e value é o valor padrão do peso das arestas
    def __init__(self,n,value):

        self.matriz = [] # Matriz de adjacentes

        self.numVertices = n # Número de Vértices do grafo (tamanho do grafo)

        try:
            for i in range(n): # n --> Número de linhas da matriz

                self.linha = [] # Lista de linhas da matriz de Adjacentes

                for j in range(n): # n --> Número de colunas da matriz

                    self.linha.append(value) # Colunas da Matriz de Adjacentes

                self.matriz.append(self.linha)

        except Exception as e:
            print("Erro ao construir o grafo ",e)

    # Método para mostrar a matriz de adjacentes
    def showMatAdj(self):
        try:
            for i in self.matriz:
                print(i)
        except Exception as e:
            print("Erro ao mostrar a matriz ",e)
    
    # Método para inserir o valor de uma aresta (weight) entre dois vértices quaisquer
    def setWeight(self,v1,v2,weight):
        try:
            self.matriz[v1][v2] = weight
            self.matriz[v2][v1] = weight
        except Exception as e:
            print("Erro ao inserir o peso da aresta ",e)

    # Método Booleano para verificar se um vértice possúi alguma ligação
    def hasAdj(self,v):
        try:
            i=0
            while(i < self.numVertices):
                # Verifica se o vértice v possúi alguma ligação (aresta) com outro vértice
                if(self.matriz[v][i] > 0):
                    return True
                i = i + 1
            return False
        except Exception as e:
            print("Não foi possível verificar os adjacentes do vértice ",e)
            return False
    
    # Método para retornar a lista de Adjacentes de um vértice em específico
    def getListAdj(self,v):
        if(self.hasAdj(v)):
            try:
                listaAdj = []
                i=0
                while(i < self.numVertices):
                    if(self.matriz[v][i] > 0):
                        listaAdj.append(i)
                    i = i + 1
                return listaAdj
            except Exception as e:
                print("Não foi possível obter a lista de Adjacentes\nMotivo: ",e)
                return None
        else:
            print("O vértice não possúi ligações")
            return None

    # Método para retornar o peso de uma ligação entre dois vértices especificados
    def getWeight(self,v1,v2):
        try:
            if(self.matriz[v1][v2] != 0):
                return (self.matriz[v1][v2])
            else:
                return None
        except Exception as e:
            print("Não foi possível retorna o valor da aresta\nMotivo: ",e)