usuarios = []
opc = -1

while opc != 0:
    print("\n--MENU--")
    print("1- Cadastrar")
    print("2- Listar Usuarios")
    print("3- Buscar Usuario")
    print("4- Remover Usuario")
    print("0- Sair")
    opc = int(input("Digite a opção desejada: "))
    
    
    match opc:
        case 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            cidade = input("Digite a cidade onde a pessoa mora: ")
            pessoa = {
                "nome": nome,
                "idade": idade,
                "cidade": cidade
            }
            usuarios.append(pessoa)
            print("Usuário cadastrado com sucesso!")
            
        case 2:
            if usuarios.__len__() == 0:
                print("Nenhum usuário cadastrado.")
            else:
                for usuario in usuarios:
                    print(f"\nInformações da pessoa {usuarios.index(usuario)+1}:")
                    print("Nome:", usuario["nome"])
                    print("Idade:", usuario["idade"])
                    print("Cidade:", usuario["cidade"])
          
        case 3:
            nome_busca = input("Digite o nome do usuário que deseja buscar: ")
            for usuario in usuarios:
                if usuario["nome"] == nome_busca:
                    print(f"Informações da pessoa {usuarios.index(usuario)+1}:")
                    print("Nome:", usuario["nome"])
                    print("Idade:", usuario["idade"])
                    print("Cidade:", usuario["cidade"])
                    break
            else:
                print("Usuário não encontrado.")
        case 4:
            nome_remover = input("Digite o nome do usuário que deseja remover: ")
            for usuario in usuarios:
                if usuario["nome"] == nome_remover:
                    usuarios.remove(usuario)
                    print("Usuário removido com sucesso!")
                    break
                else:
                    print("Usuário não encontrado.")
        case 0:
            print("Saindo do programa...")
        case _:
            print("Opção inválida. Tente novamente.")