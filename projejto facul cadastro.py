clientes = []

while True:
    print("\n--- Loja Donna Madu --")
    print("1. Inserir Cliente | 2. Consultar Cliente | 3. Atualizar Cliente | 4. Remover Cliente | 5. Listar Clientes | 0. Sair")
    opcao = input("Escolha uma opção: ") 
    

    if opcao == "1":  
        nome = input("nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cep_numeros = input("Digite o Cep: ")
        cep_formatado = f"{cep_numeros[:5]}-{cep_numeros[5:]}"
        endereco = input("Endereço: ")
        cliente = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "telefone": telefone,
            "email": email,
            "cep": cep_formatado,
            "endereco": endereco
        }
        clientes.append(cliente)
        print("Cliente inserido com sucesso!")


    elif opcao == "2":
        busca = input("Digite o nome ou CPF do cliente para consulta: ")
        for a in clientes:
            if a['nome'].lower() == busca.lower() or a['cpf'] == busca:
                print(f"localizado: {a['nome']}, CPF: {a['cpf']}, Tel: {a['telefone']}, Email: {a['email']}")
                break
        else:
            print("Cliente não encontrado!")
    
    elif opcao == "3":
        busca = input("Digite o nome ou CPF do cliente para atualizar: ")
        for a in clientes:
            if a['nome'].lower() == busca.lower() or a['cpf'] == busca:
                print(f"Editando dados de {a['nome']}")
                a['nome'] = input("Novo Nome:")
                a['data_nascimento'] = input("Nova Data de nascimento:")
                a['cpf'] = input("Novo CPF:")
                a['email'] = input("Novo Email:")
                a['telefone'] = input("Novo Telefone:")
                print("Cliente atualizado com sucesso!")
                break
        else:
            print("Cliente não encontrado! ")

    elif opcao == "4":
        nome_remover = input("Digite o nome do cliente a remover: ")
        for a in clientes:
            if a['nome'].lower() == nome_remover.lower():
                clientes.remove(a)
                print("Cliente removido com sucesso!")
                break


    elif opcao == "5":
        print("\n--- Lista de Clientes --")
        for i, a in enumerate(clientes):
            print(f"{i} - Nome: {a['nome']}, CPF: {a['cpf']}, Tel: {a['telefone']}, Email: {a['email']}")

    
#adicionar a formatação correta na digitação do cep e data de nascimento
#adicionar data de nascimento e cep na consulta e atualização
#configurar o menu para aceitar apenas números e tratar erros de digitação
#adicionar a opção de listar clientes ordenados por nome ou CPF
#adicionar a opção de salvar os dados em um arquivo e carregar os dados ao iniciar o programa
#revisar e configurar o git e gitcommit para subir o projeto no github
#horário do fim do primeiro code: 00:37 do dia 20/02/2026
#colocar comando para nao permitir numeros nos nomes e letras nos cpfs, telefones e ceps