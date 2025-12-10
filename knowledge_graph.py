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

    def remove_relationship(self, source, target, relation_type):
        if source in self.edges:
            original_len = len(self.edges[source])
            #Processo de reconstrução da lista, mantendo todas as relações exceto
            #a que queremos remover
            self.edges[source] = [ (t,r) for t,r in self.edges[source] if not(t == target and r == relation_type)]
        #Validação da remoção
            if len(self.edges[source]) < original_len:
                print("Relação removida")
            else:
                print("Relação não encontrada")
        else:
            ("Entidade não encontrada")

    def remove_entity(self, name):
        if name in self.nodes:
            #Remoção do nó e suas referências/arestas
            del self.nodes[name]
            del self.edges[name] 

            #Removendo ele dos destinos de outras aresta, ou seja, das relações
            #onde essa entidade era o objetivo da relação
            for source_node in self.edges:
                self.edges[source_node] = [(target, relation) for target, relation in self.edges[source_node] if target != name]
            print("Entidade e suas conexões removidas")
        else:
            print("Entidade não encontrada")
            