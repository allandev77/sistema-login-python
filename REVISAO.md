# Revisão do projeto

## Pontos de atenção

- `usuario` e `senha` estão definidos diretamente no arquivo `Login.py`. Mesmo que sejam credenciais de demonstração, essa prática não é adequada para um sistema real e deve ser corrigida antes de uma publicação pública se esses dados forem reais.
- O código não utiliza funções, o que é aceitável para um exercício inicial, mas dificulta a reutilização e a manutenção.
- A comparação com `False` funciona, embora a convenção Python prefira `not login`.
- Não há tratamento para entradas vazias.

## Decisão

Nenhuma alteração foi feita no código porque a solicitação foi preservar a lógica original sem autorização.

