"""Calculadora sencilla de consola con validación de datos."""


def sumar(a, b):
    """Calcula la suma de dos numeros.

        Args:
            a (float): Primer numero pedido al usuario.
            b (float): Segundo numero pedido al usuario.

        Returns: 
            float: La suma de los dos numeros del usuario.
    """
    return a + b


def restar(a, b):
    """Calcula la resta de dos numeros.
    
        Args:
            a (float): Primer numero pedido al usuario.
            b (float): Segundo numero pedido al usuario.
    
        Returns: 
            float: La resta de los dos numeros del usuario.
        """
    return a - b


def multiplicar(a, b):
    """Calcula la multiplicacion de dos numeros.
    
        Args:
            a (float): Primer numero pedido al usuario.
            b (float): Segundo numero pedido al usuario.
    
        Returns: 
            float: La multiplicacion de los dos numeros del usuario.
        """
    return a * b


def dividir(a, b):
    """Calcula la division de dos numeros.
    
        Args:
            a (float): Primer numero pedido al usuario.
            b (float): Segundo numero pedido al usuario.
    
        Returns: 
            float | str : La division de los dos numeros del usuario y Dice al usuario que no se puede dividir entre 0.
            
        """
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b


def main():
    """Ejecuta la calculadora en la consola.

    Pide al usuario dos números y vuelve a pedirlos mientras no
    introduzca un valor numérico válido. Después pide la operación
    (+, -, * o /), llama a la función correspondiente y muestra el
    resultado por pantalla. Si la operación no es válida, muestra
    un mensaje de aviso.
    """
    print("=== Calculadora ===")
    print("Operaciones disponibles: +  -  *  /")

    # Validación para el primer número (a)
    while True:
        try:
            a = float(input("Primer número: "))
            break  # Si la conversión es exitosa, sale del bucle
        except ValueError:
            print("Error: Las letras no son un tipo de dato válido. Por favor, introduce solo números.")

    # Validación para el segundo número (b)
    while True:
        try:
            b = float(input("Segundo número: "))
            break  # Si la conversión es exitosa, sale del bucle
        except ValueError:
            print("Error: Las letras no son un tipo de dato válido. Por favor, introduce solo números.")

    operacion = input("Operación: ")

    if operacion == "+":
        print("Resultado:", sumar(a, b))
    elif operacion == "-":
        print("Resultado:", restar(a, b))
    elif operacion == "*":
        print("Resultado:", multiplicar(a, b))
    elif operacion == "/":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida. Usa +, -, * o /")


if __name__ == "__main__":
    main()
