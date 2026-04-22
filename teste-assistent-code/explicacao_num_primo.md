# Explicação técnica do `num_primos.py`

Este arquivo implementa uma verificação de primalidade em Python com responsabilidade clara para cada função.

## Estrutura do código

- `eh_primo(n: int) -> bool` é a função pública que determina se `n` é primo.
- `_eh_primo_apos_tres(n: int) -> bool` é a função auxiliar que testa divisores apenas para números maiores que 3.
- `main()` contém um exemplo de uso e imprime resultados quando o arquivo é executado diretamente.

## Como `eh_primo` funciona

1. Trate casos triviais:
   - `n <= 1` retorna `False`.
   - `n <= 3` retorna `True`, porque 2 e 3 são primos.
2. Rejeite múltiplos de 2 ou 3 imediatamente:
   - `n % 2 == 0` ou `n % 3 == 0` retornam `False`.
3. Delegue a verificação restante para `_eh_primo_apos_tres`.

## Como `_eh_primo_apos_tres` funciona

- O algoritmo testa apenas divisores na forma `6k - 1` e `6k + 1`.
- Começa com `divisor = 5` e aumenta `divisor` em 6 a cada passo.
- Para cada valor de `divisor`, ele verifica `n % divisor == 0` e `n % (divisor + 2) == 0`.
- O loop termina quando `divisor * divisor > n`, pois não há necessidade de testar divisores maiores que a raiz quadrada de `n`.

## Por que isso é mais limpo

- A separação em funções deixa cada parte com uma única responsabilidade.
- O nome `_eh_primo_apos_tres` explica claramente que a função trata apenas o caso posterior aos primeiros valores.
- O bloco `main()` centraliza o comportamento de execução direta, deixando a função `eh_primo` reutilizável em outros módulos.

## Exemplo de saída esperada

Quando executado diretamente, o programa imprime:

- `1 é primo? False`
- `2 é primo? True`
- `3 é primo? True`
- `4 é primo? False`
- `17 é primo? True`
- `18 é primo? False`
- `19 é primo? True`
- `20 é primo? False`
