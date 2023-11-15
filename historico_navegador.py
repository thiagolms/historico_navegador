from pilha import Pilha

class HistoricoNavegador:
    def __init__(self):
        self.pilha_paginas = Pilha()

    def adicionar_pagina(self, pagina):
        self.pilha_paginas.empilhar(pagina)

    def voltar_pagina(self):
        try:
            pagina_atual = self.pilha_paginas.desempilhar()
            pagina_anterior = self.pilha_paginas.topo()
            print("Voltando para:", pagina_anterior)
            self.pilha_paginas.empilhar(pagina_atual)
            return self.pilha_paginas.desempilhar()
        except IndexError:
            print("Não há páginas anteriores no histórico.")

    def avancar_pagina(self):
        if self.pilha_paginas.tamanho() > 1:
            pagina_atual = self.pilha_paginas.topo()
            proxima_pagina = self.pilha_paginas.desempilhar()
            print("Avançando para:", proxima_pagina)
            self.pilha_paginas.empilhar(pagina_atual)
            return proxima_pagina
        else:
            print("Não há páginas seguintes no histórico.")
            return None
        pass

    def visualizar_historico(self):
        print("Histórico de Navegação:")
        for pagina in reversed(self.pilha_paginas.itens):
            print(pagina)

    def pagina_atual(self):
        try:
            return self.pilha_paginas.topo()
        except IndexError:
            print("A pilha está vazia. Nenhuma página atual.")
            return None
