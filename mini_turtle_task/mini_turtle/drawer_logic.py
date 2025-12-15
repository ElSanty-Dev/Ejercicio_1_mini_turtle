posicion_horizontal = 0

def adelante(n):
    global posicion_horizontal
    # Dibuja espacios hasta la posición actual y luego el tramo horizontal
    print(" " * posicion_horizontal + "-" * n + ">")
    posicion_horizontal += n

def abajo(n):
    # Dibuja el descenso vertical alineado al final del escalón
    for _ in range(n):
        print(" " * posicion_horizontal + "|")

posicion_horizontal = 0

def reiniciar():
    global posicion_horizontal
    posicion_horizontal = 0
    print("🐢 Posición reiniciada a 0")
