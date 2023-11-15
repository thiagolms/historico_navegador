from historico_navegador import HistoricoNavegador

historico = HistoricoNavegador()

historico.adicionar_pagina("www.exemplo.com/pagina1")
historico.adicionar_pagina("www.exemplo.com/pagina2")
historico.adicionar_pagina("www.exemplo.com/pagina3")
historico.adicionar_pagina("www.exemplo.com/pagina4")


historico.visualizar_historico()

print("Página atual:", historico.pagina_atual())

historico.voltar_pagina()
print("Página após voltar:", historico.pagina_atual())

historico.avancar_pagina()
print("Página após avançar:", historico.pagina_atual())

historico.visualizar_historico()
