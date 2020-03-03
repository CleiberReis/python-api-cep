import requests

def main():
    print()

    print('#####################')
    print('### Consulta CEP ####')
    print('#####################')
    print()

    cep_input = input('Digite um cep para a consulta: ')

    print()

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida')
        option = int(input('Deseja tentar novamente?\n1. Sim\n2. Não\n'))

        if option == 1:
            main()
        else:
            print('Até logo!...')
            exit()

    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('######################')
        print('==> CEP ENCONTRADO <==')
        print('######################')
        print()
        print('CEP: {}'.format(address_data['cep']))
        print('Rua: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
        print()
        print('######################')
        print()
    else:
        print('##########################')
        print('==> CEP NÃO ENCONTRADO <==')
        print('##########################')
        print()
        print('Verifique o CEP digitado, pois {} é um CEP inválido.'.format(cep_input))
        print()
        print('##########################')

    option = int(input('Deseja realizar uma nova consulta?\n1. Sim\n2. Não\n'))

    if option == 1:
        main()
    else:
        print('Encerrando...')
        exit()


if __name__ == "__main__":
    main()
