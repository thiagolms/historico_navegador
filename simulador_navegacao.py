from historico_navegador import HistoricoNavegador

def abrir_nova_pagina(historico):
    nova_pagina = input("Digite o URL da nova página: ")
    if nova_pagina:
        historico.adicionar_pagina(nova_pagina)
        print(f"Nova página aberta: {nova_pagina}")

def voltar_pagina(historico):
    historico.voltar_pagina()

def avancar_pagina(historico):
    historico.avancar_pagina()
   

def visualizar_historico(historico):
    historico.visualizar_historico()

def sair(historico):
    print("Saindo do simulador de navegador.")
    exit()

def exibir_menu():
    print("\nMenu:")
    print("1. Abrir Nova Página")
    print("2. Voltar Página")
    print("3. Avançar Página")
    print("4. Visualizar Histórico")
    print("0. Sair")

def main():
    historico = HistoricoNavegador()

    opcoes = {
        1: abrir_nova_pagina,
        2: voltar_pagina,
        3: avancar_pagina,
        4: visualizar_historico,
        0: sair,
    }

    while True:
        exibir_menu()
        escolha = int(input("Escolha uma opção: "))

        funcao = opcoes.get(escolha, lambda: print("Opção inválida."))
        funcao(historico)

if __name__ == "__main__":
    main()
