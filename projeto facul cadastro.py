#cliente teste
def gerar_cliente_teste():
    return {
        "nome": "Usuário de Teste",
        "cpf": "12345678900",
        "data_nascimento": "01011990",
        "cep": "12345678",
        "endereco": "Rua de Teste, 123",
        "email": "test@dominio.com",
        "telefone": "000000000"
    }
clientes = []

while True:
    print("\n--- Loja Donna Madu --")
    print("1. Inserir Cliente | 2. Consultar Cliente | 3. Atualizar Cliente | 4. Remover Cliente | 5. Listar Clientes | 0. Sair")
    opcao = input("Escolha uma opção: ") 
    

    if opcao == "1":  
        nome = input("nome: ")
        data_nascimento = input("Data de nascimento: ")
        data_nascimento_formatada = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
        cpf_numeros = input("CPF: ")
        cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
        email = input("Email: ")
        telefone = input("Telefone: ")
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        cep_numeros = input("Digite o Cep: ")
        cep_formatado = f"{cep_numeros[:5]}-{cep_numeros[5:]}"
        endereco = input("Endereço: ")
        numero_residencia = input("Número da residência: ")
        endereco_completo = f"{endereco}, {numero_residencia}"
        informaçoes_adicionais = input("Informações adicionais: ")
        
        cliente = {
            "nome": nome,
            "cpf": cpf_formatado,
            "data_nascimento": data_nascimento_formatada,
            "telefone": telefone_formatado,
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
                print(f"localizado: {a['nome']}, CPF: {a['cpf']}, Data de Nascimento: {a['data_nascimento']}, CEP: {a['cep']}, Endereço: {a['endereco']}, Telefone: {a['telefone']}, Email: {a['email']}")
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
            print(f"{i} - Nome: {a['nome']}, CPF: {a['cpf']}, Data de Nascimento: {a['data_nascimento']}, CEP: {a['cep']}, Tel: {a['telefone']}, Email: {a['email']}")

    
#adicionar data de nascimento e cep na consulta e atualização
#configurar o menu para aceitar apenas números e tratar erros de digitação
#adicionar a opção de listar clientes ordenados por nome ou CPF
#adicionar a opção de salvar os dados em um arquivo e carregar os dados ao iniciar o programa
#revisar e configurar o git e gitcommit para subir o projeto no github
#horário do fim do primeiro code: 00:37 do dia 20/02/2026
#colocar comando para nao permitir numeros nos nomes e letras nos cpfs, telefones e ceps