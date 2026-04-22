from collections import namedtuple
from typing import List

Estatisticas = namedtuple('Estatisticas', ['total', 'media', 'maior', 'menor'])

def calcular_estatisticas(numeros: List[int]) -> Estatisticas:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros: Lista de números inteiros.

    Returns:
        Estatisticas: Tupla nomeada com total, média, maior e menor valor.

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return Estatisticas(total, media, maior, menor)

def main():
    """Função principal para executar o cálculo e exibir os resultados."""
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    stats = calcular_estatisticas(numeros)
    print(f"Total: {stats.total}")
    print(f"Média: {stats.media}")
    print(f"Maior: {stats.maior}")
    print(f"Menor: {stats.menor}")

if __name__ == "__main__":
    main()