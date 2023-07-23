#Criar estrutura para armazenar os roteadores e suas conexões
#conectionsRouter = [{'roteador': 'A', 'conexoes': ['B', 'C', 'D'], 'distancia':[3,5,6]}, {'roteador': 'B', 'conexoes': ['A', 'C', 'D'], 'distancia':[4,5,5]}]

def addConection(conectionsRouter: list, router: str, connection: list, values: list) -> list:
    if not conectionsRouter:
        conectionsRouter.append({"roteador": router, "conexoes": connection,"distancia": values})
    elif conectionsRouter[0]["roteador"] == router:
        pass
    else:
        conectionsRouter[1:] = addConection(conectionsRouter[1:], router, connection,values)
    return conectionsRouter

def addConectionFromRouter(conectionsRouter: list, routerOrigin,routerDestiny: str,valueRouterDestiny: str)->list:
    if conectionsRouter:
        if routerOrigin == conectionsRouter[0]["roteador"] and not routerDestiny in conectionsRouter[0]["conexoes"]:
            conectionsRouter[0]["conexoes"].append(routerDestiny)
            conectionsRouter[0]["distancia"].append(valueRouterDestiny)
        elif routerOrigin == conectionsRouter[0]["roteador"] and routerDestiny in conectionsRouter[0]["conexoes"]:
            pass
        else:
            conectionsRouter[1:] = addConectionFromRouter(conectionsRouter[1:], routerOrigin,routerDestiny,valueRouterDestiny)
    return conectionsRouter

def existsRouter(conectionsRouter:list,routerOrigin:str,routerDestiny:str,valueRouterDestiny:str)->list: 
    if any(dicionario.get('roteador') == routerDestiny for dicionario in conectionsRouter) : 
        conectionsRouter = addConectionFromRouter(conectionsRouter,routerOrigin,routerDestiny,valueRouterDestiny)
    return conectionsRouter

 #Remove a rota para o roteador, de todos os outros roteadores
def removeConectionFromRouter(conectionsRouter: list, routerOrigin,routerDestiny: str) -> list:
    if conectionsRouter:
        if routerOrigin == conectionsRouter[0]["roteador"] and routerDestiny in conectionsRouter[0]["conexoes"]:
            indexRouter = conectionsRouter[0]["conexoes"].index(routerDestiny)
            conectionsRouter[0]["conexoes"].pop(indexRouter)
            conectionsRouter[0]["distancia"].pop(indexRouter)
        else: 
            conectionsRouter[1:] = removeConectionFromRouter(conectionsRouter[1:], routerOrigin,routerDestiny)
    return conectionsRouter

def removeConection(conectionsRouter:list, router:str):
    if conectionsRouter:
        if router in conectionsRouter[0]["conexoes"]:
            indexRouter = conectionsRouter[0]["conexoes"].index(router)
            conectionsRouter[0]["conexoes"].pop(indexRouter)
            conectionsRouter[0]["distancia"].pop(indexRouter)    
        conectionsRouter[1:] = removeConection(conectionsRouter[1:], router)
    return conectionsRouter


def filter_router(router_to_remove: str, router_entry: dict) -> bool:
    if router_entry["roteador"] == router_to_remove:
        return False
    return True

def removeRouter(conectionsRouter: list, router: str) -> list:
    new_connections_router = list(filter(lambda entry: filter_router(router, entry), conectionsRouter))
    new_connections_router = removeConection(new_connections_router, router)
    return new_connections_router

def listConections(conectionsRouter: list):
    if conectionsRouter:
        print(F'Roteador : {conectionsRouter[0]["roteador"]} | ')
        listRouterDistance(conectionsRouter[0]["conexoes"],conectionsRouter[0]["distancia"])
        listConections(conectionsRouter[1:])

def listRouterDistance(conections:list,distances:list):
    if conections and distances:
        print(F'conectado ao roteador {conections[0]}',end=" ")
        print(F'com distância de {distances[0]}m |')
        listRouterDistance(conections[1:],distances[1:])

def menu(conectionsRouter:list):
    print("1 - Adicionar roteador")#Adiciona o dicionário roteador e suas conexões
    print("2 - Remover roteador")#Apaga o dicionário roteador, suas conexões, e a rota dos demais roteadores para ele
    print("3 - Adicionar rota a um roteador")#Adiciona a rota de um roteador para outro, pendente
    print("4 - Remover rota de um roteador")#Remove a rota de um roteador para outro
    print("5 - Listar roteadores e suas conexões")#Passa por todos os dicionários e imprime o roteador e suas conexões
    print("6 - Menores rotas")#Usa o algorimto de dijkstra para calcular a menor rota de todos os roteadores
    print("7 - Sair")
    try:
        option = int(input("Digite a opção desejada: "))
        if option < 1 or option > 7:
            print("Opção inválida")
            return menu(conectionsRouter)
        if option == 1:
            router = input("Digite o nome do roteador: ")
            connections = input("Digite a conexão(use ',' para separar): ")
            connections = connections.split(',')
            values = input("Digite as distâncias(use ',' para separar): ")
            values = values.split(',')
            conectionsRouter = addConection(conectionsRouter, router, connections, values)
            return menu(conectionsRouter)
        if option == 2:
            router = input("Digite o nome do roteador: ")
            conectionsRouter = removeRouter(conectionsRouter, router)
            return menu(conectionsRouter)
        if option == 3:
            routerOrigin = input("Digite o nome do roteador: ")
            routerDestiny = input("Rota a ser adicionada : ")
            valueRouterDestiny = input("Distância da rota: ")
            conectionsRouter = existsRouter(conectionsRouter,routerOrigin,routerDestiny,valueRouterDestiny)
            return menu(conectionsRouter)
        if option == 4:
            routerOrigin = input("Digite o nome do roteador: ")
            routerDestiny = input("Rota a ser removida : ")
            conectionsRouter = removeConectionFromRouter(conectionsRouter,routerOrigin,routerDestiny)
            return menu(conectionsRouter)
        if option == 5:
            listConections(conectionsRouter)
            return menu(conectionsRouter)
        if option == 6:
            print("Em construção")
            return menu(conectionsRouter)
        if option == 7:
            return
    except ValueError:
        print("Apenas valore inteiros podem ser utilizados para operar o menu")
        return menu(conectionsRouter)
    return option

if __name__ == '__main__':
    conectionsRouter = []
    menu(conectionsRouter)