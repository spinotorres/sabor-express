import os

restaurantes = ['Burger King', 'McDonalds', 'Subway', 'Habib\'s']

def exibir_titulo():
    print('/\/\/\/\- SABOR EXPRESS -/\/\/\/\ \n')

def exibir_menu():
    print(  '1. Cadastrar restaurante\n' + 
            '2. Listar restaurantes\n' + 
            '3. Ativar restaurante\n' +
            '4. Sair\n')

def voltar_menu():
    input('\n------------ Pressione enter para voltar ao menu ------------')

def opcao_invalida():
    print('OPÇÃO INVALIDA!\n')
    voltar_menu()

def exibir_subtitulo(subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(subtitulo)

def cadastrar_restaurante():
    exibir_subtitulo('---------------- Cadastro de novo restaurante ----------------\n')
    restaurante = input("Nome do restaurante: ")
    restaurantes.append(restaurante)
    print(f'\nO restaurante {restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('-------------------- Lista de restaurantes --------------------\n')
    if len(restaurantes) <= 0:
        print('Nenhum restaurante cadastrado!\n')
    else:
        for i, restaurante in enumerate(restaurantes, 1):
            print(f"{i}. {restaurante}")
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
