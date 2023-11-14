from pilha import Pilha

class HistoricoNavegador:
    def __init__(self):
        self.pilha_paginas = Pilha()

    def adicionar_pagina(self, pagina):
        self.pilha_paginas.empilhar(pagina)

    def voltar_pagina(self):
        try:
            return self.pilha_paginas.desempilhar()
        except IndexError:
            print("Não há páginas anteriores no histórico.")

    def avancar_pagina(self):
        if self.pilha_paginas.tamanho() > 1:
            pagina_atual = self.pilha_paginas.desempilhar()
            proxima_pagina = self.pilha_paginas.topo()
            
            print("Avançando para:", proxima_pagina)
            self.pilha_paginas.empilhar(pagina_atual)
        else:
            print("Não há páginas seguintes no histórico.")
        pass

    def visualizar_historico(self):
        print("Histórico de Navegação:")
        for pagina in reversed(self.pilha_paginas.itens):
            print(pagina)
