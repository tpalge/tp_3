visitar_nulo = lambda a,b,c,d: True
heuristica_nula = lambda actual,destino: 0

class Grafo(object):
    '''Clase que representa un grafo. El grafo puede ser dirigido, o no, y puede no indicarsele peso a las aristas
    (se comportara como peso = 1). Implementado como "diccionario de diccionarios"'''
    
    def __init__(self, es_dirigido = False):
        '''Crea el grafo. El parametro 'es_dirigido' indica si sera dirigido, o no.'''
        self.es_dirigido = es_dirigido
		self.vertices = {}
    
    def __len__(self):
        '''Devuelve la cantidad de vertices del grafo'''
        return len(self.vertices)
    
    def __iter__(self):
        '''Devuelve un iterador de vertices, sin ningun tipo de relacion entre los consecutivos'''
		return iter(self.vertices.keys)
	               
    def keys(self):
        '''Devuelve una lista de identificadores de vertices. Iterar sobre ellos es equivalente a iterar sobre el grafo.'''
        id_vertices = []
		for v in self.vertices:
			id_vertices.append(v)
        
    def __getitem__(self, id):
        '''Devuelve el valor del vertice asociado, del identificador indicado. Si no existe el identificador en el grafo, lanzara KeyError.'''
        if id not in self.vertices:
			return KeyError
		return self.vertices[id][0]
    
    def __setitem__(self, id, valor):
        '''Agrega un nuevo vertice con el par <id, valor> indicado. ID debe ser de identificador unico del vertice.
        En caso que el identificador ya se encuentre asociado a un vertice, se actualizara el valor.
        '''
		self.vertices[id] = [valor, {}]
    
    def __delitem__(self, id):
        '''Elimina el vertice del grafo. Si no existe el identificador en el grafo, lanzara KeyError.
        Borra tambien todas las aristas que salian y entraban al vertice en cuestion.
        '''
		for v in self.vertices:
			if v != id:
				if id in self.vertices[v][1]:
					self.vertices[v][1].pop(id)			
		
		for ady in self.vertices[id][1]:
			self.vertices[id][1].pop(ady)

        self.vertices.pop(id)
			
    
    def __contains__(self, id):
        ''' Determina si el grafo contiene un vertice con el identificador indicado.'''
		if id in self.vertices.keys:
			return True
		
		return False
        
    def agregar_arista(self, desde, hasta, peso = 1):
        '''Agrega una arista que conecta los vertices indicados. Parametros:
            - desde y hasta: identificadores de vertices dentro del grafo. Si alguno de estos no existe dentro del grafo, lanzara KeyError.
            - Peso: valor de peso que toma la conexion. Si no se indica, valdra 1.
            Si el grafo es no-dirigido, tambien agregara la arista reciproca.
        '''
        self.vertices[desde][1][hasta] = peso
		if not self.es_dirigido:
			self.vertices[hasta][1][desde] = peso
        
    def borrar_arista(self, desde, hasta):
        '''Borra una arista que conecta los vertices indicados. Parametros:
            - desde y hasta: identificadores de vertices dentro del grafo. Si alguno de estos no existe dentro del grafo, lanzara KeyError.
           En caso de no existir la arista, se lanzara ValueError.
        '''
        raise NotImplementedError()
    
    def obtener_peso_arista(self, desde, hasta):
        '''Obtiene el peso de la arista que va desde el vertice 'desde', hasta el vertice 'hasta'. Parametros:
            - desde y hasta: identificadores de vertices dentro del grafo. Si alguno de estos no existe dentro del grafo, lanzara KeyError.
            En caso de no existir la union consultada, se devuelve None.
        '''
		if desde in self.vertices and hasta in self.vertices:
			#if hasta in adyacentes(self,desde):  
			if hasta in self.vertices[desde][1].keys:  
				return self.vertices[desde][1][hasta]
			else:
				return None
		
        raise KeyError()
    
    def adyacentes(self, id):
        '''Devuelve una lista con los vertices (identificadores) adyacentes al indicado. Si no existe el vertice, se lanzara KeyError'''
		if id not in self.vertices.keys:
			raise KeyError()
			
		adyacentes = []
		
		for vecino in self.vertices[id][1].keys:
			adyacentes.append(vecino)
		
        return adyacentes
		
	
	def recorrido(self, tipo_recorrido):
    visitados = {} #diccionario
    padre = {}
    orden = {}
    for v in self.vertice:
        if v not in visitados:
            padre[v] = None
            orden[v] = 0
			if tipo_recorrido == 0:
				bfs_visitar(self, v, visitados, padre, orden)
			else:
				dfs_visitar(self, v, visitados, padre, orden)
				
    return padre, orden

	def bfs(self, visitar = visitar_nulo, extra = None, inicio=None):	
	    '''Realiza un recorrido BFS dentro del grafo, aplicando la funcion pasada por parametro en cada vertice visitado.
        Parametros:
            - visitar: una funcion cuya firma sea del tipo: 
                    visitar(v, padre, orden, extra) -> Boolean
                    Donde 'v' es el identificador del vertice actual, 
                    'padre' el diccionario de padres actualizado hasta el momento,
                    'orden' el diccionario de ordenes del recorrido actualizado hasta el momento, y 
                    'extra' un parametro extra que puede utilizar la funcion (cualquier elemento adicional que pueda servirle a la funcion a aplicar). 
                    La funcion aplicar devuelve True si se quiere continuar iterando, False en caso contrario.
            - extra: el parametro extra que se le pasara a la funcion 'visitar'
            - inicio: identificador del vertice que se usa como inicio. Si se indica un vertice, el recorrido se comenzara en dicho vertice, 
            y solo se seguira hasta donde se pueda (no se seguira con los vertices que falten visitar)
        Salida:
            Tupla (padre, orden), donde :
                - 'padre' es un diccionario que indica para un identificador, cual es el identificador del vertice padre en el recorrido BFS (None si es el inicio)
                - 'orden' es un diccionario que indica para un identificador, cual es su orden en el recorrido BFS
        '''
		padre,orden = recorrido(self, 0, inicio, visitar, extra)   
        return padre,orden

	def bfs_visitar(self, origen, visitados, padre, orden):
		q = Cola()
		q.encolar(origen)
		visitados[origen] = True
		while len(cola) > 0:
			v = cola.desencolar()
			for w in adyacentes(self,v):
				if w not in visitados:
					visitados[w] = True
					padre[w] = v
					orden[w] = orden[v] + 1
					q.encolar(w)
		
	def dfs_visitar(self, vertice, estados_vertices):
		estados_vertices[vertice] = 2
		
		for vecino in adyacentes(self,vertice):
			if estados_vertices[vecino] == 1:
				dfs_visitar(self,vecino,estados_vertices)
		
		estados_vertices[vertice] = 3
		
	def dfs(self, visitar = visitar_nulo, extra = None, inicio=None):
        '''Realiza un recorrido DFS dentro del grafo, aplicando la funcion pasada por parametro en cada vertice visitado.
        - visitar: una funcion cuya firma sea del tipo: 
                    visitar(v, padre, orden, extra) -> Boolean
                    Donde 'v' es el identificador del vertice actual, 
                    'padre' el diccionario de padres actualizado hasta el momento,
                    'orden' el diccionario de ordenes del recorrido actualizado hasta el momento, y 
                    'extra' un parametro extra que puede utilizar la funcion (cualquier elemento adicional que pueda servirle a la funcion a aplicar). 
                    La funcion aplicar devuelve True si se quiere continuar iterando, False en caso contrario.
            - extra: el parametro extra que se le pasara a la funcion 'visitar'
            - inicio: identificador del vertice que se usa como inicio. Si se indica un vertice, el recorrido se comenzara en dicho vertice, 
            y solo se seguira hasta donde se pueda (no se seguira con los vertices que falten visitar)
        Salida:
            Tupla (padre, orden), donde :
                - 'padre' es un diccionario que indica para un identificador, cual es el identificador del vertice padre en el recorrido DFS (None si es el inicio)
                - 'orden' es un diccionario que indica para un identificador, cual es su orden en el recorrido DFS
        '''
        
		# 1 = blanco, 2 = gris, 3 = negro
		
		estados_vertices = {}
		
		for vertice in self.vertices:
			estados_vertices[vertice] = 1
			
		for vertice in self.vertice:
			if estados_vertices[vertice] == 1:
				visitar(vertice,)
			
    
    def componentes_conexas(self):
        '''Devuelve una lista de listas con componentes conexas. Cada componente conexa es representada con una lista, con los identificadores de sus vertices.
        Solamente tiene sentido de aplicar en grafos no dirigidos, por lo que
        en caso de aplicarse a un grafo dirigido se lanzara TypeError'''
        raise NotImplementedError()
        
    def camino_minimo(self, origen, destino, heuristica=heuristica_nula):
        '''Devuelve el recorrido minimo desde el origen hasta el destino, aplicando el algoritmo de Dijkstra, o bien
        A* en caso que la heuristica no sea nula. Parametros:
            - origen y destino: identificadores de vertices dentro del grafo. Si alguno de estos no existe dentro del grafo, lanzara KeyError.
            - heuristica: funcion que recibe dos parametros (un vertice y el destino) y nos devuelve la 'distancia' a tener en cuenta para ajustar los resultados y converger mas rapido.
            Por defecto, la funcion nula (devuelve 0 siempre)
        Devuelve:
            - Listado de vertices (identificadores) ordenado con el recorrido, incluyendo a los vertices de origen y destino. 
            En caso que no exista camino entre el origen y el destino, se devuelve None. 
        '''
        raise NotImplementedError()
    
    def mst(self):
        '''Calcula el Arbol de Tendido Minimo (MST) para un grafo no dirigido. En caso de ser dirigido, lanza una excepcion.
        Devuelve: un nuevo grafo, con los mismos vertices que el original, pero en forma de MST.'''
        raise NotImplementedError()
    
    def random_walk(self, largo, origen = None, pesado = False):
        ''' Devuelve una lista con un recorrido aleatorio de grafo.
            Parametros:
                - largo: El largo del recorrido a realizar
                - origen: Vertice (id) por el que se debe comenzar el recorrido. Si origen = None, se comenzara por un vertice al azar.
                - pesado: indica si se tienen en cuenta los pesos de las aristas para determinar las probabilidades de movernos de un vertice a uno de sus vecinos (False = todo equiprobable). 
            Devuelve:
                Una lista con los vertices (ids) recorridos, en el orden del recorrido. 
        '''
        raise NotImplementedError()
