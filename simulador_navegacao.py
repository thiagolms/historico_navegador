from historico_navegador import HistoricoNavegador

historico = HistoricoNavegador()

historico.adicionar_pagina("www.exemplo.com/pagina1")
historico.adicionar_pagina("www.exemplo.com/pagina2")
historico.adicionar_pagina("www.exemplo.com/pagina3")

historico.visualizar_historico()

pagina_anterior = historico.voltar_pagina()
print("Voltando para:", pagina_anterior)

pagina_posterior = historico.avancar_pagina()

historico.visualizar_historico()
