#Criar estrutura para armazenar os roteadores e suas conexões
conectionsRouter = [{'roteador': 'A', 'conexoes': ['B', 'C', 'D'], 'distancia':[3,5,6]}, {'roteador': 'B', 'conexoes': ['A', 'C', 'D'], 'distancia':[4,5,5]}]

def addConection(conectionsRouter: list, router: str, connection: list, values: list) -> list:
    if not conectionsRouter:
        conectionsRouter.append({"roteador": router, "conexoes": connection,"distancia": values})
    elif conectionsRouter[0]["roteador"] == router:
        pass
    else:
        conectionsRouter[1:] = addConection(conectionsRouter[1:], router, connection,values)
    return conectionsRouter


def filter_router(router_to_remove: str, router_entry: dict) -> bool:
    if router_entry["roteador"] == router_to_remove:
        return False
    return True

def removeConection(conectionsRouter: list, router: str) -> list:
    new_connections_router = list(filter(lambda entry: filter_router(router, entry), conectionsRouter))
    return new_connections_router

def listConections(conectionsRouter: list):
    if conectionsRouter:
        print(F'Roteador : {conectionsRouter[0]["roteador"]} | ')
        conections = conectionsRouter[0]["conexoes"].split(',')
        distances = conectionsRouter[0]["distancia"].split(',')
        listRouterDistance(conections,distances)
        listConections(conectionsRouter[1:])

def listRouterDistance(conections:list,distances:list):
    if conections and distances:
        print(F'conectado ao roteador {conections[0]}',end=" ")
        print(F'com distância de {distances[0]}m |')
        listRouterDistance(conections[1:],distances[1:])

def menu(conectionsRouter:list):
    #Permitir adicionar e remover a conexão de um roteador
    print("1 - Adicionar roteador")
    print("2 - Remover roteador")#Apaga o dicionário roteador e suas conexões, mas os roteadores conectaos a ele ainda permanecem
    print("3 - Listar roteadores e suas conexões")
    print("4 - Menores rotas")#Usa o algorimto de dijkstra para calcular a menor rota de todos os roteadores
    print("5 - Sair")
    option = int(input("Digite a opção desejada: "))
    if option < 1 or option > 5:
        print("Opção inválida")
        return menu(conectionsRouter)
    if option == 1:
        router = input("Digite o nome do roteador: ")
        connections = input("Digite a conexão(use ',' para separar): ")
        values = input("Digite as distâncias(use ',' para separar): ")
        conectionsRouter = addConection(conectionsRouter, router, connections, values)
        return menu(conectionsRouter)
    if option == 2:
        router = input("Digite o nome do roteador: ")
        conectionsRouter = removeConection(conectionsRouter, router)
        return menu(conectionsRouter)
    if option == 3:
        listConections(conectionsRouter)
        return menu(conectionsRouter)
    return option

if __name__ == '__main__':
    conectionsRouter = []
    menu(conectionsRouter)