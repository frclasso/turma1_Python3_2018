"""O que acontece com a agenda se ocorrer um erro de leitura ou
gravação? Explique.

Resposta:
Em caso de erro de leitura, o programa pára de executar.
Se o erro ocorrer durante a gravação, os dados não gravados
serão perdidos.
Estes problemas podem ser resolvidos com a alteração das
funções de leitura e gravação, adicionando-se blocos try/except
O ideal é que o programa exiba a mensagem de erro e continue rodando.
No caso da gravação, os dados não devem ser perdidos e o usuário deve poder
tentar novamente.

"""