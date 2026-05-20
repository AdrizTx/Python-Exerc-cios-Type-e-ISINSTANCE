# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.

print("\n\n")
print("======== EXERCICIO 1 ========")
print("\n\n")

ano = 2024
print("ano: ", ano)
print("Tipo: ", type(ano))

# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().

print("\n\n")
print("======== EXERCICIO 2 ========")
print("\n\n")

num = 3.14159
print("O numero 3.14159 é um numero tipo float?")
print("Verificando...")
print(isinstance(num, float))

# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.

print("\n\n")
print("======== EXERCICIO 3 ========")
print("\n\n")

resultado1 = type(100) == type(True)
print("tipo de 100 é igual o tipo de True?")
print("Verificando...")
print("resultado: ", resultado1)


# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.

print("\n\n")
print("======== EXERCICIO 4 ========")
print("\n\n")

resultado2 = isinstance(True, int)
print("True pode ser considerado int?")
print("Verificando...")
print("resultado: ", resultado2)

# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().

print("\n\n")
print("======== EXERCICIO 5 ========")
print("\n\n")

resultado3 = 5/2
print("tipo Float(Utilizando Type): ", type(resultado3))
print("tipo Float(Utilizando isinstance): ", isinstance(resultado3,float))

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.

print("\n\n")
print("======== EXERCICIO 6 ========")
print("\n\n")

def verificar_numero(valor):
    if isinstance(valor, (int, float, complex)):
        print("É número!")
verificar_numero(10)
verificar_numero(3.14)
verificar_numero(2 + 5j)
verificar_numero("texto")

# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

print("\n\n")
print("======== EXERCICIO 7 ========")
print("\n\n")

valor = True
print(type(valor) == int)
print(isinstance(valor, int))

# EX8
# Descubra o tipo do número 3+4j
# usando type().

print("\n\n")
print("======== EXERCICIO 8 ========")
print("\n\n")

numero = 3+4j
print(type(numero))

# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().

print("\n\n")
print("======== EXERCICIO 9 ========")
print("\n\n")

valor = None
print(isinstance(valor, type(None)))

# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.

print("\n\n")
print("======== EXERCICIO 10 ========")
print("\n\n")

numero = 3.0
print(isinstance(numero, (int, float, complex)))
print(isinstance(numero, int))
