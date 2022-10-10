Forma = str(input('''Escolha qual poligono ira aparecer!

Digitando : 

Q/q = Quadrado

T/t = Triangulo

L/l = Losango

H/h = Hexagono

O/o = Octogono

TR/tr/Tr/tR = Triangulo Reto

QV/qv/Qv/qV = Quadrado Vazio

TV/tv/Tv/tV = Triangulo Vazio

= '''))

print()

Formato = str(input('''Escolha apenas um caracter para compor o formato de seu poligono! 
= '''))

print()

# quadrado
if Forma == "Q" or Forma == "q":
    A = int(input('''Qual o tamanho do lado do quadrado? 
= '''))
    S = 0

# triangulo
if Forma == "T" or Forma == "t":
    A = int(input('''Qual a altura do triangulo? 
= '''))
    B = A
    S = 1

# losango
if Forma == "L" or Forma == "l":
    A = int(input('''Qual tamanho do lado do losango? 
= '''))
    B = A
    S = 1

# hexagono
if Forma == "H" or Forma == "h":
    A = int(input('''Qual o tamanho do lado do hexagono? 
= '''))
    B = A
    L = A
    S = 0

# octogono
if Forma == "O" or Forma == "o":
    A = int(input('''Qual o tamanho do lado do hexagono? 
= '''))
    B = A
    L = A
    S = 0

# triangulo reto
if Forma == "TR" or Forma == "tr" or Forma == "Tr" or Forma == "tR":
    A = int(input('''Qual a altura do triangulo reto? 
= '''))
    L = 1
    S = 0

# quadrado vazio
if Forma == "QV" or Forma == "qv" or Forma == "Qv" or Forma == "qV":
    A = int(input('''Qual a altura do triangulo vazio? 
= '''))
    B = A - 2
    S = 0

# triangulo vazio
if Forma == "TV" or Forma == "tv" or Forma == "Tv" or Forma == "tV":
    A = int(input('''Qual a altura do triangulo vazio? 
= '''))
    B1 = A - 1
    S = 0

print('''
''')

# quadrado
if Forma == "Q" or Forma == "q":
    for i in range(A):
        print(Formato * A)
        S = S + A

    print('''
    ''')
    print(f"Quadrado composto por {S} caracteres do tipo ({Formato})")

# triangulo
if Forma == "T" or Forma == "t":
    print(" " * B, end="")
    print(Formato)
    L = 3

    for i in range(1, A):
        B = B - 1
        print(" " * B, end="")
        print(Formato * L)
        S = S + L
        L = L + 2

    print('''
    ''')
    print(f"Triangulo composto por {S} caracteres do tipo ({Formato})")

# losango
if Forma == "L" or Forma == "l":
    print(" " * B, end="")
    print(Formato)
    L = 3

    for i in range(1, A):
        B = B - 1
        print(" " * B, end="")
        print(Formato * L)
        S = S + L
        L = L + 2

    B = B + 1
    L = L - 2

    for i in range(1, A):
        print(" " * B, end="")
        B = B + 1
        L = L - 2
        S = S + L
        print(Formato * L)

    print('''
    ''')
    print(f"Losango composto por {S} caracteres do tipo ({Formato})")

# hexagono
if Forma == "H" or Forma == "h":
    for i in range(A):
        B = B - 1
        print(" " * B, end="")
        print(Formato * L)
        S = S + L
        L = L + 2

    L = L - 2

    for i in range(A - 1):
        B = B + 1
        print(" " * B, end="")
        L = L - 2
        S = S + L
        print(Formato * L)

    print('''
    ''')
    print(f"Hexagono composto por {S} caracteres do tipo ({Formato})")

# octogono
if Forma == "O" or Forma == "o":
    for i in range(A):
        B = B - 1
        print(" " * B, end="")
        print(Formato * L)
        S = S + L
        L = L + 2

    L = L - 2

    for i in range(A - 1):
        print(Formato * L)
        S = S + L

    for i in range(A - 1):
        B = B + 1
        print(" " * B, end="")
        L = L - 2
        S = S + L
        print(Formato * L)

    print('''
    ''')
    print(f"Octogono composto por {S} caracteres do tipo ({Formato})")

# triangulo reto
if Forma == "TR" or Forma == "tr" or Forma == "Tr" or Forma == "tR":
    for i in range(A):
        print(Formato * L)
        S = S + L
        L = L + 1

    print('''
    ''')
    print(f"Triangulo Reto composto por {S} caracteres do tipo ({Formato})")

# quadrado vazio
if Forma == "QV" or Forma == "qv" or Forma == "Qv" or Forma == "qV":
    if A == 1:
        print("* ")
        print(" *")
    else:
        print(Formato * A)
        for i in range(A - 2):
            print(Formato, end="")
            print(" " * B, end="")
            print(Formato)
            S = S + 1

        print(Formato * A)
        S = (S * 2) + (A * 2)
        print('''
        ''')
        print(f"Quadrado Vazio composto por {S} caracteres do tipo ({Formato})")

# triangulo vazio
if Forma == "TV" or Forma == "tv" or Forma == "Tv" or Forma == "tV":
    print(" " * B1, end="")
    B1 = B1 - 1
    print(Formato)
    B2 = 1

    for i in range(A - 2):
        print(" " * B1, end="")
        B1 = B1 - 1
        print(Formato, end="")
        print(" " * B2, end="")
        B2 = B2 + 2
        print(Formato)
        S = S + 1

    print(Formato * (B2 + 2))
    S = (S * 2) + 1 + B2 + 2
    print('''
    ''')
    print(f"Triangulo Vazio composto por {S} caracteres do tipo ({Formato})")
