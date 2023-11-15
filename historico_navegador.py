from pilha import Pilha

class HistoricoNavegador:
    def __init__(self):
        self.pilha_paginas_visitadas = Pilha()
        self.pilha_paginas_futuras = Pilha()

    def adicionar_pagina(self, pagina):
        self.pilha_paginas_visitadas.empilhar(pagina)
        # Ao adicionar uma nova página, limpa a pilha de páginas futuras
        self.pilha_paginas_futuras = Pilha()

    def voltar_pagina(self):
        try:
            pagina_atual = self.pilha_paginas_visitadas.desempilhar()
            pagina_atualv = self.pilha_paginas_visitadas.topo()
            print("Voltando para:", pagina_atualv)
            self.pilha_paginas_futuras.empilhar(pagina_atual)
            return pagina_atual
        except IndexError:
            print("Não há páginas anteriores no histórico.")

    def avancar_pagina(self):
        try:
            pagina_futura = self.pilha_paginas_futuras.desempilhar()
            print("Avançando para:", pagina_futura)
            self.pilha_paginas_visitadas.empilhar(pagina_futura)
            return pagina_futura
        except IndexError:
            print("Não há páginas seguintes no histórico.")
            return None

    def visualizar_historico(self):
        print("Histórico de Navegação:")
        for pagina in reversed(self.pilha_paginas_visitadas.itens):
            print(pagina)

    def pagina_atual(self):
        try:
            return self.pilha_paginas_visitadas.topo()
        except IndexError:
            print("A pilha está vazia. Nenhuma página atual.")
            return None