import os

restaurantes = [{'Nome':'Jojo Ramen', 'Categoria':'Japonesa', 'Status':False},
                {'Nome':'Quintal do Braz', 'Categoria':'Italiana', 'Status':True},
                {'Nome':'Halim', 'Categoria':'Arabe', 'Status':False}]

def exibir_titulo():
    print('/\/\/\/\- SABOR EXPRESS -/\/\/\/\ \n')

def exibir_menu():
    print(  '1. Cadastrar restaurante\n' + 
            '2. Listar restaurantes\n' + 
            '3. Ativar restaurante\n' +
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
    status_restaurante = input(f"O restaurante {nome_restaurante} está ativo? Digite (S/N): ")


    restaurantes.append(nome_restaurante)
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
            atividade_restaurante = 'Ativo' if restaurante['Ativo'] else 'Inativo'
            print(f'{i}. {nome_restaurante} | {categoria_restaurante} | {atividade_restaurante}')
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
                    print('Ativar restaurante')
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
