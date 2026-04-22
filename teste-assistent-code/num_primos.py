from __future__ import annotations

def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return _eh_primo_apos_tres(n)


def _eh_primo_apos_tres(n: int) -> bool:
    """Testa divisores na forma 6k-1 e 6k+1 para n > 3."""
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def main() -> None:
    numeros = [1, 2, 3, 4, 17, 18, 19, 20]
    for num in numeros:
        print(f'{num} é primo? {eh_primo(num)}')


if __name__ == '__main__':
    main()
