from search_functions import DBZ_Search

class Knowledge_Graph:
    def __init__(self):
        self.nodes = {} #Dicionário dos nós
        self.edges = {} #Dicionário das arestas de relações

    def add_entity(self, name, properties = {}):
         if name not in self.nodes:
             self.nodes[name] = properties #Propriedades do nó
             self.edges[name] = [] #Conexões
             print(f"Entidade {name} adicionada")
             
    def add_relationship(self, source, target, relation_type):
        if source in self.nodes and target in self.nodes:
            self.edges[source].append((target, relation_type))
            print("Relação adicionada")
        else:
            print("Uma das entidades não existe")

    def get_relationships(self, entity_name):
        if entity_name in self.nodes:
            return self.edges[entity_name]
        return None
