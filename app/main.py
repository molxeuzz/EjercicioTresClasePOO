from app.model import Partida, JuegoAdivinanza, Jugador

def main():
    nombre = input("Ingrese su nombre: ")
    jugador = Jugador(nombre)
    partida = Partida()
    juego = JuegoAdivinanza()

    while True:
        print("\n1. Hacer un intento")
        print("2. Mostrar puntaje")
        print("3. Mostrar intentos realizados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                intento = int(input("Ingrese un número entre 1 y 100: "))
                if 1 <= intento <= 100:
                    print(juego.verificar_intento(intento, jugador, partida))
                else:
                    print("Número fuera de rango. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número válido.")
        elif opcion == "2":
            print(jugador.mostrar_puntaje())
        elif opcion == "3":
            print("Intentos realizados:", partida.mostrar_intentos())
        elif opcion == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
