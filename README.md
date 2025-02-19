# Enunciado del Ejercicio: Juego de Adivinanza con Registro de Intentos

## Descripción General
El objetivo de este ejercicio es desarrollar un juego en consola llamado **"Adivina el Número"** utilizando **Programación Orientada a Objetos (POO)** en Python.  

En este juego, el jugador intentará adivinar un número secreto generado aleatoriamente entre **1 y 100**. Cada intento es registrado y se proporciona retroalimentación indicando si el número ingresado es **mayor o menor** que el número secreto.  

Cuando el jugador acierta, **gana un punto** y se genera un nuevo número secreto.

---

## Requisitos del Sistema

El sistema debe contar con las siguientes clases:

### **Clase `Jugador`**
#### **Atributos:**
- `nombre` (*str*): Nombre del jugador.
- `puntaje` (*int*): Puntos obtenidos al adivinar correctamente el número.

#### **Métodos:**
- `incrementar_puntaje()`: Aumenta en 1 el puntaje del jugador cuando acierta.
- `mostrar_puntaje()`: Devuelve una cadena indicando la cantidad de puntos del jugador.

---

### **Clase `Partida`**
#### **Atributos:**
- `intentos` (*list*): Lista de números ingresados por el jugador durante la partida.

#### **Métodos:**
- `registrar_intento(intento: int)`: Almacena cada intento en la lista.
- `mostrar_intentos()`: Devuelve una lista de los intentos realizados o un mensaje si no hay intentos.

---

### **Clase `JuegoAdivinanza`**
#### **Atributos:**
- `nombre` (*str*): Nombre del juego.
- `numero_secreto` (*int*): Número aleatorio generado entre **1 y 100**.

#### **Métodos:**
- `verificar_intento(intento: int, jugador: Jugador, partida: Partida)`:  
  - Compara el intento con el número secreto.
  - Si es menor, indica que el número es mayor.
  - Si es mayor, indica que el número es menor.
  - Si acierta, incrementa el puntaje del jugador y genera un nuevo número secreto.

---

## **Interacción con el Usuario (Menú de Opciones)**
El sistema debe permitir la interacción con el usuario mediante un **menú en la consola** con las siguientes opciones:

### **1. Hacer un intento**
- El jugador ingresa un número y recibe una pista de si el número secreto es **mayor o menor**.
- Si acierta, gana un punto y se genera un nuevo número secreto.

### **2. Mostrar puntaje**
- Se muestra la cantidad de puntos acumulados por el jugador.

### **3. Mostrar intentos realizados**
- Se muestra la lista de intentos realizados por el jugador durante la partida.

### **4. Salir**
- Finaliza la ejecución del programa.

---

## **Restricciones**
- El número secreto **debe regenerarse** después de cada acierto.
- Se debe validar que el usuario ingrese un número en el rango de **1 a 100**.
- Se debe manejar correctamente la entrada de datos del usuario para evitar errores.
