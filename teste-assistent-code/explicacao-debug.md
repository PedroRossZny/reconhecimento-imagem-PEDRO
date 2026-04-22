# Explicação dos Erros no Código debug.py

## Erros Identificados

1. **Erro de Sintaxe na Linha 6**:
   - Código: `item1 = float(input(Preço do item 1? ))`
   - Problema: Falta as aspas duplas ao redor da string "Preço do item 1? ". Em Python, strings devem estar entre aspas.
   - Correção: `item1 = float(input("Preço do item 1? "))`

2. **Erro de Tipo na Variável desconto_cupom (Linha 18)**:
   - Código: `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - Problema: A função `input()` retorna uma string, mas o código tenta usar `desconto_cupom` como um número em operações matemáticas (divisão por 100) e comparações (desconto_cupom > 0).
   - Correção: Converter para float: `desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`

3. **Erro de Sintaxe na Linha 27**:
   - Código: `print(" Item 2:        R$ {total_item2:.2f}")`
   - Problema: Falta o prefixo `f` antes da string para que seja uma f-string. Sem isso, as chaves não são interpoladas.
   - Correção: `print(f" Item 2:        R$ {total_item2:.2f}")`

4. **Erro de Lógica na Condição if (Linha 32)**:
   - Código: `if desconto_cupom > 0:`
   - Problema: Como `desconto_cupom` era uma string, a comparação não funcionaria corretamente. Mesmo após correção, se o usuário digitar 0, deve ser tratado como sem desconto.
   - Correção: Após converter para float, a comparação funcionará, mas garantir que seja numérica.

5. **Erro de Formatação na Linha 33**:
   - Código: `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
   - Problema: `desconto_cupom` era uma string, então não pode ser formatado como `.0f`. Após correção para float, isso será resolvido.

6. **Problema de Indentação na Linha 33**:
   - Código: `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
   - Problema: A linha está indentada incorretamente dentro do bloco if, mas em Python, a indentação deve ser consistente (geralmente 4 espaços).
   - Correção: Ajustar a indentação para 4 espaços.

7. **Uso Desnecessário de round() na Linha 36**:
   - Código: `print(f" TOTAL:         R$ {round(total, 2):.2f}")`
   - Problema: O formatador `.2f` já arredonda para 2 casas decimais, então `round(total, 2)` é redundante.
   - Correção: Remover o `round()`: `print(f" TOTAL:         R$ {total:.2f}")`

## Resumo

O código tinha principalmente erros de sintaxe (aspas faltando, f-string incompleta), problemas de tipo (string usada como número) e questões de formatação. Após as correções, o código deve funcionar corretamente para calcular o total de uma compra com itens, imposto e desconto opcional.
