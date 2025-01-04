import os

restaurantes = [{'Nome':'Jojo Ramen', 'Categoria':'Japonesa', 'Status':False},
                {'Nome':'Quintal do Braz', 'Categoria':'Italiana', 'Status':True},
                {'Nome':'Halim', 'Categoria':'Arabe', 'Status':False}]

def exibir_titulo():
    print('/\/\/\/\- SABOR EXPRESS -/\/\/\/\ \n')

def exibir_menu():
    print(  '1. Cadastrar restaurante\n' + 
            '2. Listar restaurantes\n' + 
            '3. Ativar restaurante ou Desativar restaurante\n' +
            '4. Sair\n')

def voltar_menu():
    input('\n------------ Pressione enter para voltar ao menu ------------')

def exibir_subtitulo(subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(subtitulo)

def cadastrar_restaurante():
    exibir_subtitulo('---------------- Cadastro de novo restaurante ----------------\n')

    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_do_restaurante = {'Nome': nome_restaurante, 'Categoria': categoria_restaurante, 'Status': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('-------------------- Lista de restaurantes --------------------\n')
    if len(restaurantes) <= 0:
        print('Nenhum restaurante cadastrado!\n')
    else:
        for i, restaurante in enumerate(restaurantes, 1):
            nome_restaurante = restaurante['Nome']
            categoria_restaurante = restaurante['Categoria']
            status_restaurante = 'Ativo' if restaurante['Status'] else 'Inativo'
            print(f'{i}. {nome_restaurante} | {categoria_restaurante} | {status_restaurante}')
    voltar_menu()

def alterar_status_restaurante():
    exibir_subtitulo('------------------ Alterar status do restaurante ------------------\n')
    listar_restaurantes()
    restaurante_escolhido = int(input('Digite o número do restaurante que deseja alterar o status: '))
    if restaurante_escolhido > len(restaurantes) or restaurante_escolhido <= 0:
        print('Restaurante não encontrado!\n')
    else:
        restaurante = restaurantes[restaurante_escolhido - 1]
        nome_restaurante = restaurante['Nome']
        status_restaurante = 'Ativo' if restaurante['Status'] else 'Inativo'
        print(f'\nRestaurante {nome_restaurante} está {status_restaurante}')
        novo_status = 'Ativo' if not restaurante['Status'] else 'Inativo'
        restaurante['Status'] = not restaurante['Status']
        print(f'\nStatus do restaurante {nome_restaurante} alterado para {novo_status}\n')
    voltar_menu()

def opcao_invalida():
    print('OPÇÃO INVALIDA!\n')
    voltar_menu()

def finalizar_aplicativo():
    exibir_subtitulo('------------------- Aplicativo finalizado -------------------\n')

def escolher_opcao():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir_titulo()
            exibir_menu()
            opcao_escolhida = int(input('Escolha uma opção: '))
            
            match opcao_escolhida:
                case 1:
                    cadastrar_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    alterar_status_restaurante()
                case 4:
                    finalizar_aplicativo()
                    break
                case _:
                    opcao_invalida ()
                    
        except ValueError:
            opcao_invalida()

def main():
    escolher_opcao()


if __name__ == "__main__":
    main()
