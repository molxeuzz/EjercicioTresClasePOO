
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def incrementar_puntaje(self):
        self.puntaje += 1

    def mostrar_puntaje(self):
        return f"{self.nombre} tiene {self.puntaje} puntos."

class Partida:
    def __init__(self):
        self.intentos = []

    def registrar_intento(self, intento):
        self.intentos.append(intento)

    def mostrar_intentos(self):
        return self.intentos if self.intentos else "No hay intentos aún."

import random

class JuegoAdivinanza:
    def __init__(self):
        self.nombre = "Adivina el Número"
        self.numero_secreto = random.randint(1, 100)

    def verificar_intento(self, intento, jugador, partida):
        partida.registrar_intento(intento)
        if intento < self.numero_secreto:
            return "El número secreto es mayor."
        elif intento > self.numero_secreto:
            return "El número secreto es menor."
        else:
            jugador.incrementar_puntaje()
            self.numero_secreto = random.randint(1, 100)
            return "¡Correcto! Has ganado un punto y se ha generado un nuevo número secreto."
