def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota invalida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada invalida! Digite um numero.")


def calcular_situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERACAO"
    else:
        return "REPROVADO"


def main():
    print("=" * 40)
    print("   CALCULADORA DE MEDIA SEMESTRAL")
    print("=" * 40)

    nome = input("Nome do aluno: ")

    nota1 = ler_nota(1)
    nota2 = ler_nota(2)

    media = (nota1 + nota2) / 2
    situacao = calcular_situacao(media)

    print("\n" + "=" * 40)
    print(f"  Aluno: {nome}")
    print(f"  Nota 1: {nota1:.1f}")
    print(f"  Nota 2: {nota2:.1f}")
    print(f"  Media:  {media:.2f}")
    print(f"  Situacao: {situacao}")
    print("=" * 40)


if __name__ == "__main__":
    main()
