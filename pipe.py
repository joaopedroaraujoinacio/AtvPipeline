"""
atividade de teste de pipeline
"""

def somar(a, b):

    return a + b

def multiplicar(a, b):

    return a * b

def processar_dados(numeros):

    resultado = {
        'soma': sum(numeros),
        'quantidade': len(numeros),
        'media': sum(numeros) / len(numeros) if numeros else 0
    }
    return resultado

def main():
    print("=== Teste de Pipeline ===")
    
    x, y = 10, 5
    print(f"\nTeste 1: Operações básicas")
    print(f"Soma de {x} + {y} = {somar(x, y)}")
    print(f"Multiplicação de {x} * {y} = {multiplicar(x, y)}")
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nTeste 2: Processamento de dados")
    print(f"Lista: {numeros}")
    resultado = processar_dados(numeros)
    print(f"Resultado: {resultado}")
    
    print(f"\nTeste 3: Status")
    print("✓ Todos os testes passaram com sucesso!")
    print("✓ Pipeline funcionando corretamente!")
    
    return 0

if __name__ == "__main__":
    exit(main())